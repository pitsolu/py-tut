import bcrypt

def makeHash(password):
	salt = bcrypt.gensalt()
	return bcrypt.hashpw(password, salt) # Hash password

def checkHash(password, password_hash):
	return bcrypt.checkpw(password, password_hash)