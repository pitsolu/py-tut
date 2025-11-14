import json

from flask import Flask, request, session
from src.app.models import *
from src.app.helpers import *
from fs import open_fs as ofs

app = Flask(__name__)
app.secret_key = ofs(".").open("app.key").read().encode("utf-8")

@app.route("/")
def index():
    return "Hello World"

@app.route("/user/<id>")
def get_user(id):
    try:
        # u=User.getById(id)
        u=User.getOneBy("id", id)
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
        session['username'] = username
        return json.dumps({'message':'User logged in successfully.'})
    else:
        return json.dumps({'message':'Failed to login!'})

@app.route("/user/status")
def status():
    if 'username' in session:
        username = session['username']
        return json.dumps({'message':f"current user[{username}]."})
    return json.dumps({'message':"No user!"})

@app.route("/logout", methods=['POST'])
def logout():
    username = None
    if 'username' in session:
        username = session['username']
        session.pop('username', None)
        return json.dumps({'message':f'User[{username}] logged out!'})
    return json.dumps({'message':'No user'})