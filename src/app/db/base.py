import camelsnake
import logging

from pypika import Query, Table, Field, Criterion, Parameter
from dotenv import dotenv_values
from src.app.db.sqlite import Wrapper as W
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

class GateWay:
	rows = []

class Base:
	_join = []
	_db = SqliteDb().getDb()
	def __init__(self, row):
		self.gateway = {}
		self.load(row)
		if len(self._join) > 0:
			foreign_id = self._join.pop()
			field, _ = foreign_id.split("_")
			module = __import__("src.app.models", fromlist=[""])
			foreign_class = getattr(module, field.capitalize())
			setattr(self, field, foreign_class.getById(row[foreign_id]))

	@property
	def db(self):
		return _db

	def load(self, row=None):
		if row is not None:
			for key, value in row.items():
				if hasattr(self, key):
					setattr(self, key, value)
				else:
					if key.endswith("_id"):
						self._join.append(key)

	@classmethod
	def getById(sclass, id):
		table = camelsnake.camel_to_snake(sclass.__name__)
		table = Table(table)

		sql = str(Query.from_(table).select("*").where(table.id == Parameter("?")))
		logger.debug([sql, id])

		row = sclass._db.getOne(sql, (id,))
		return sclass(row)

	def dump(self):
		return self.__dict__

	def save(self):
		props = self.dump()
		table = Table(camelsnake.camel_to_snake(self.__class__.__name__))

		sql = str(Query.into(table).columns(*props.keys()).insert(Qmarks(len(props))))

		params = list(props.values())
		if hasattr(self, "id"):
			self.id = props.pop("id")
			fields = list(props.keys())
			fields.remove("id")
			sql = str(QmarksUp(Query.update(table), fields)
						.where(Criterion.all([table.id==Parameter("?")])))

		logger.debug([sql, params])

		cursor = self._db.exec(sql, params)
		if sql.startswith("INSERT"):
			self.id = cursor.lastrowid