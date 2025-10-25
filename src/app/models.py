from src.app.helpers import *
from src.app.db.base import Base

class User(Base):
	def __init__(self, row=None):
		self.email = None
		self.password = None
		super().__init__(row)

	def checkPassword(self, password):
		return checkHash(password, self.password)

	def getByEmail(email):
		row = self.db.getOne(f"SELECT * FROM user WHERE email = ?", (email,))
		return User(row)

# class User:
# 	def __init__(self, email, password):
# 		self.email = email
# 		self.password = password

# 	def getEmail(self):
# 		return self.email

# 	def checkPassword(self, password):
# 		return checkHash(password, self.password)