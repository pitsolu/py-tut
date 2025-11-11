import camelsnake

from src.app.helpers import *
from src.app.db.base import *
from src.app.db.qb import *

@column("name")
@column("status")
@column("created_at")
class Permission(Base):
	def __init__(self, row=None):
		super().__init__(row)


@column("name")
@column("descr")
class Role(Base):
	def __init__(self, row=None):
		super().__init__(row)

	def getPermissions(self):
		return[role_perm.permission for role_perm in RolePermission.getManyBy("role_id", self.id)]

@column("created_at")
@refer("role_id")
@refer("permission_id")
class RolePermission(Base):
	role:Role = None
	permission:Permission = None
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