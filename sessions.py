import sqlite3
import json
from flask import Flask, request
from flask_cors import CORS


con = sqlite3.connect("todoapp.db")
cur = con.cursor()

def initSessions(app):
    @app.route('/sessions', methods=['POST'])
    def create_session():
        data = request.get_json()
        print(data)
        con = sqlite3.connect("todoapp.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        res = cur.execute("SELECT * FROM users WHERE email=? AND password=?", [data['email'], data['password']]).fetchall()
        if len(res) == 0:
            return "invalid email or password"

        cur.execute("INSERT INTO sessions(user_id) VALUES(?)", [res[0]['id']])
        con.commit()
        return {"id": cur.lastrowid}
        print("Session Created")
        results = [dict(row) for row in res]
        return results