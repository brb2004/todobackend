import sqlite3
class SessionsRepos:
    @staticmethod
    def create(session):
        con = sqlite3.connect("todoapp.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("INSERT INTO sessions(user_id) VALUES(?)", [session["id"]])
        con.commit()

        return  {
            "id": cur.lastrowid,
        }

    def get(id):
        con = sqlite3.connect("todoapp.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        res = cur.execute("SELECT * FROM sessions WHERE id=?", [id])
        return  dict(res.fetchone())