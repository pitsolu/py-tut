import camelsnake

from src.app.helpers import *
from src.app.db.base import *
from src.app.db.qb import *

@column("name")
@column("descr")
# @column("status")
class Role(Base):
	def __init__(self, row=None):
		super().__init__(row)


@column("username")
@column("password")
@column("status")
@refer("role_id")
class User(Base):
	role: Role = None
	def __init__(self, row=None):
		super().__init__(row)

	def checkPassword(self, password):
		return checkHash(password, self.password)

	def getByUsername(username):
		return User.getOneBy("username", username)