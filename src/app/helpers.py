import bcrypt
import camelsnake

from pypika import QmarkParameter, Parameter

def makeHash(password):
	salt = bcrypt.gensalt()
	return bcrypt.hashpw(password, salt) # Hash password

def checkHash(password, password_hash):
	return bcrypt.checkpw(password, password_hash)

# ignore
def Qmarks(count):
	r=[]
	for i in range(count):
		r.append(QmarkParameter())
	return r


# ignore
def QmarksUp(qb, fields):
	for field in fields:
		qb = qb.set(field, Parameter('?'))
	return qb

# @columns decorator/annotation for models
def column(field, value = None):
	def class_decorator(cls):
		table = camelsnake.camel_to_snake(cls.__name__)
		cls._props.append(table + "." + field)
		setattr(cls, field, value)
		return cls
	return class_decorator