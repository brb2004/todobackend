import sqlite3
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:5174'])
@app.route('/todos')
def todos():
    con = sqlite3.connect("todoapp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    res = cur.execute("SELECT * FROM todos")
    results = [dict(row) for row in res.fetchall()]
    return results
@app.route('/todos/<id>')
def todo(id):
    con = sqlite3.connect("todoapp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    res = cur.execute("SELECT * FROM todos WHERE id=?", [id])
    results = [dict(row) for row in res.fetchall()]
    return results
@app.route('/')
def index():
    return ""
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    con = sqlite3.connect("todoapp.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("INSERT INTO todos(item) VALUES(?)", [data['item']])
    con.commit()
    response = {'message': 'Data Received','data':data}
    return json.dumps(response), 201

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
