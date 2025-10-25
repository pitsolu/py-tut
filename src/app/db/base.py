import camelsnake
import logging

from dotenv import dotenv_values
from src.app.db.sqlite import Wrapper as W

logger = logging.getLogger(__name__)
logging.basicConfig(filename='logs/app.log', level=logging.INFO)

class Base:
	config = dotenv_values(".env")
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
		row = sclass._db.getOne(f"SELECT * FROM {table} WHERE id = ?", (id,))
		return sclass(row)

	def dump(self):
		return self.__dict__

	def save(self):
		props = self.dump()
		attrs = ", ".join(props.keys())
		delims = ", ".join(["?"] * len(props))
		table = camelsnake.camel_to_snake(self.__class__.__name__)

		sql = f"INSERT INTO {table}({attrs}) values({delims})"

		params = list(props.values())
		if hasattr(self, "id"):
			id = props.pop("id")
			fields = props.keys()
			attrs = " = ?, ".join(fields) + " = ?"
			sql = f"UPDATE {table} SET {attrs} WHERE id = ?"
			self.id = id

		logger.info([sql, params])

		cursor = self._db.exec(sql, params)
		if sql.startswith("INSERT"):
			self.id = cursor.lastrowid