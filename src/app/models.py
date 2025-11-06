import camelsnake

from src.app.helpers import *
from src.app.db.base import Base, SqliteDb

@column("name")
@column("descr")
# @column("status")
class Role(Base):
	def __init__(self, row=None):
		super().__init__(row)


@column("username")
@column("password")
@column("status")
class User(Base):
	role: Role = None
	def __init__(self, row=None):     
		super().__init__(row)

	def checkPassword(self, password):
		return checkHash(password, self.password)

	def getByUsername(username):
		# q = Query.from_(u).left_join(r).on(u.role_id == r.id).select(u.star, r.name)
		sql = "SELECT u.id, u.username, u.password FROM user u WHERE u.username = ?"
		row = SqliteDb().getDb().getOne(sql, (username,))

		return User(row)