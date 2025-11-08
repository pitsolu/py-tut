import camelsnake
import logging
import inspect

from pypika import Query, Table, Field, Criterion, Parameter
from dotenv import dotenv_values
from src.app.db.sqlite import Wrapper as W
from src.app.db.qb import *
from src.app.helpers import Qmarks, QmarksUp

config = dotenv_values(".env")
logger = logging.getLogger(__name__)
logging.basicConfig(filename=config["LOG"], format='%(asctime)s|%(levelname)s:%(name)s %(message)s')
logger.setLevel(int(config["LOG_LVL"]))

class SqliteDb:
	def __init__(self):
		pass

	def getDb(self):
		return W(config["DB"])

class Gateway:
	tables = []
	def __init__(self, row):
		self.row = row
		self.models_module = __import__("src.app.models", fromlist=[""])
		for obj in inspect.getmembers(self.models_module, inspect.isclass):
			if issubclass(obj[1], Base) and obj[0]!="Base":
				self.tables.append(camelsnake.camel_to_snake(obj[1].__name__))

	def getTables(self):
		return self.tables

	@classmethod
	def makeRow(sclass, row, table):
		table+="_"
		return {key.replace(table,''): row[key] for key in row.keys() if key.startswith(table)}

	def getRset(self):
		rset={}
		for table in self.getTables():
			rset[table]=Gateway.makeRow(self.row, table)

		return rset

	def makeModel(self, aggr):
		rset = self.getRset()
		_class = getattr(self.models_module, aggr)
		table = camelsnake.camel_to_snake(aggr)
		inst = _class(rset[table])

		rset.pop(table)
		okeys = rset.keys()
		for key in okeys:
			if hasattr(inst, key):
				model = str(camelsnake.snake_to_camel(key)).capitalize()
				setattr(inst, key, self.makeModel(model))

		return inst


class Base:
	id=None
	_db = SqliteDb().getDb()
	def __init__(self, row):
		self.load(row)

	@property
	def db(self):
		return _db

	def load(self, row=None):
		if row is not None:
			for key, value in row.items():
				if hasattr(self, key):
					setattr(self, key, value)

	@classmethod
	def getById(sclass, id):
		table = camelsnake.camel_to_snake(sclass.__name__)
		table = Table(table)

		sql = str(Query.from_(table).select("*").where(table.id == Parameter("?")))
		logger.debug([sql, id])

		row = sclass._db.getOne(sql, (id,))
		return sclass(row)

	@classmethod
	def getOneBy(sclass, field, value):
		module = __import__("src.app.models", fromlist=[""])
		qb = Qb(sclass)
		for ref in sclass._refer:
			table, _ = ref.split("_")
			model = getattr(module, camelsnake.snake_to_camel(table).capitalize())
			qb.leftjoin(model)

		sql = str(qb.where(field))
		logger.debug([sql, value])

		row = SqliteDb().getDb().getOne(sql, (value,))

		return Gateway(row).makeModel(sclass.__name__)

	def dump(self):
		return self.__dict__

	def save(self):
		props = self.dump()
		table = Table(camelsnake.camel_to_snake(self.__class__.__name__))

		id=None
		if "id" in props.keys():
			id = props.pop("id") 

		if id is None:
			sql = str(Query.into(table).columns(*props.keys()).insert(Qmarks(len(props))))

		params = list(props.values())
		if hasattr(self, "id"):
			if id is not None:
				fields = list(props.keys())
				sql = str(QmarksUp(Query.update(table), fields)
							.where(Criterion.all([table.id==Parameter("?")])))
				params.append(id)

		logger.debug([sql, params])

		cursor = self._db.exec(sql, params)
		if sql.startswith("INSERT"):
			self.id = cursor.lastrowid