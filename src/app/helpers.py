import bcrypt

from pypika import QmarkParameter, Parameter


def makeHash(password):
	salt = bcrypt.gensalt()
	return bcrypt.hashpw(password, salt) # Hash password

def checkHash(password, password_hash):
	return bcrypt.checkpw(password, password_hash)

def Qmarks(count):
	r=[]
	for i in range(count):
		r.append(QmarkParameter())
	return r

def QmarksUp(qb, fields):
	for field in fields:
		qb = qb.set(field, Parameter('?'))
	return qb