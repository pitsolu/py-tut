import camelsnake
import logging

from pypika import Query, Table, Field, QmarkParameter, Criterion, Parameter
from dotenv import dotenv_values
from src.app.db.sqlite import Wrapper as W
from src.app.helpers import Qmarks, QmarksUp

config = dotenv_values(".env")
logger = logging.getLogger(__name__)
logging.basicConfig(filename=config["LOG"], format='%(asctime)s|%(levelname)s:%(name)s %(message)s')
logger.setLevel(int(config["LOGLVL"]))

class Base:
	_db = W(config["DB"])
	def __init__(self, row):
		self.load(row)    	

	@property
	def db(self):
		return _db

	def load(self, row=None):
		if row is not None:
			for key, value in row.items():
				setattr(self, key, value)

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