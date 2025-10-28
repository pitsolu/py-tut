from src.app.helpers import *
from src.app.db.base import Base, SqliteDb

class Role(Base):
	def __init__(self, row=None):
		self.name = None
		self.descr = None
		super().__init__(row)

class User(Base):
	role: Role = None
	def __init__(self, row=None):
		self.email = None
		self.password = None      
		super().__init__(row)
		# self.role = self.getEntity("Role", self.role_id)

	def checkPassword(self, password):
		return checkHash(password, self.password)

	def getByEmail(email):
		# q = Query.from_(u).left_join(r).on(u.role_id == r.id).select(u.star, r.name)
		sql = "SELECT u.id, u.email, u.password FROM user u WHERE u.email = ?"
		row = SqliteDb().getDb().getOne(sql, (email,))

		return User(row)