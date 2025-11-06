import json

from flask import Flask, request
from src.app.models import *
from src.app.helpers import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/user/<id>")
def get_user(id):
    try:
        u=User.getById(id)
        u.role = u.role.dump()
        del u.password
        return json.dumps(u.dump())
    except:
        return json.dumps({'message':'User does not exist!'})

@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    u = User.getByUsername(username)
    if u.checkPassword(password.encode("utf-8")):
        return json.dumps({'message':'User logged in successfully.'})
    else:
        return json.dumps({'message':'Failed to login!'})