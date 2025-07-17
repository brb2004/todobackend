import sqlite3
import json
from flask import Flask, request
from flask_cors import CORS
from sessions import initSessions
from src.routes.users_routes import UsersRoutes
from src.routes.todos_routes import TodosRoutes

import wtforms_json
wtforms_json.init()
app = Flask(__name__)
CORS(app, origins=['http://localhost:5174'])

initSessions(app)

TodosRoutes(app)
UsersRoutes(app)



@app.route('/')
def index():
    return ""
    con = sqlite3.connect("todoapp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    res = cur.execute("SELECT * FROM sessions WHERE id=?", [authorization])
    session = dict(res.fetchone())

    res = cur.execute("SELECT * FROM users WHERE id=?", [session['user_id']])
    return dict(res.fetchone())

@app.route('/todos/<id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    con = sqlite3.connect("todoapp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("UPDATE todos SET item=? WHERE id=?", [data["item"], id])
    con.commit()
    return json.dumps(True), 201

@app.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    con = sqlite3.connect("todoapp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("DELETE FROM todos WHERE id=?", [id])
    con.commit()
    return json.dumps(True), 201

@app.route('/todoappuser/<id>')
def todoappuser(id):
    con = sqlite3.connect("todoapp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    res = cur.execute("SELECT * FROM users WHERE id=?", [id])
    results = [dict(row) for row in res.fetchall()]
    return results



@app.route('/todoappuser/<id>', methods=['PUT'])
def update_todoappuser(id, email, password):
    data = request.get_json()
    con = sqlite3.connect("todoapp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("UPDATE users SET email, password=?  WHERE id=?",email, password, id)
    con.commit()

    return json.dumps(True), 201

#@app.route('/random')
#def random():
#    user = current_user()
 ##       return unauthorized()

 #   con = sqlite3.connect("todoapp.db")
 #   con.row_factory = sqlite3.Row
 #   cur = con.cursor()
  #  res = cur.execute("SELECT * FROM todos WHERE user_id = ? ORDER BY RANDOM() LIMIT 1", [user["id"]])
  ##  return results