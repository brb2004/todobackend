import sqlite3
class UsersRepos:
    @staticmethod
    def create(user):
        con = sqlite3.connect("todoapp.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("INSERT INTO users(email,password) VALUES(?, ?)", (user["email"], user["password"]))
        con.commit()

        return  {
            "id": cur.lastrowid,
            "email": user["email"],
            "password": user["password"],

        }

    def get(id):
        con = sqlite3.connect("todoapp.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        res = cur.execute("SELECT * FROM users WHERE id=?", [id])
        return dict(res.fetchone())