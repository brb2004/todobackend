import sqlite3
import json
from flask import request

class TodosRepos:

    @staticmethod
    def get(user):
        con = sqlite3.connect("todoapp.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        res = cur.execute("SELECT * FROM todos WHERE user_id = ?", [user["id"]])
        return [dict(row) for row in res.fetchall()]

    def todo(id):
        con = sqlite3.connect("todoapp.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        res = cur.execute("SELECT * FROM todos WHERE id=?", [id])
        results = [dict(row) for row in res.fetchall()]
        return results

    @staticmethod
    def create_todo(user, todo):
        data = request.get_json()
        print(data)
        con = sqlite3.connect("todoapp.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        res = cur.execute("SELECT * FROM categories WHERE name=?", [todo["category"]])
        category = res.fetchone()

        if category:
            category_id = dict(category)["id"]
        else:
            cur.execute("INSERT INTO categories (name) VALUES (?)", [todo["category"]])
            con.commit()
            category_id = cur.lastrowid

        cur.execute("INSERT INTO todos(item, category_id, user_id) VALUES(?, ?, ?)", [todo['item'], category_id, user['id']])
        con.commit()
        return todo
