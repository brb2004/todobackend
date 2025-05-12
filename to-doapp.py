import sqlite3
con = sqlite3.connect("todoapp.db")
cur = con.cursor()
#cur.execute("DROP TABLE todos")
#cur.execute("CREATE TABLE todos(id INTEGER PRIMARY KEY AUTOINCREMENT,item)")
#cur.execute("INSERT INTO todos(item) VALUES(2)")
#con.commit()
#cur.execute("INSERT INTO todos(item) VALUES(1)")
#con.commit()
#res = cur.execute("SELECT * FROM todos")
#print(res.fetchall())
#exit(1)


x = None

while True:
    print("\nWhat would you like to do?\n1: Add to List\n2: Remove from list\n3: Delete List\n4: View List\n5: Update List \n6: Exit ")
    a = int(input("What would you like to do: "))
    if a == 1:
        while x !="Done":
            x = str(input("Enter an activity: "))
            cur.execute("INSERT INTO todos(item) VALUES(?)", [x])
            con.commit()
            res = cur.execute("SELECT * FROM todos")
            print(res.fetchall())
            if x == "Done":
                break
    elif a == 2:
        print("\nWhat would you like to delete?")
        x = str(input("Enter an item: "))
        cur.execute("DELETE FROM todos WHERE id=?", [x])
        con.commit()
        res = cur.execute("SELECT * FROM todos")
        print(res.fetchall())

    elif a == 3:
        cur.execute("DELETE FROM todos")
        cur.execute("DELETE FROM SQLITE_SEQUENCE WHERE name='todos';")
        con.commit()
    elif a == 4:
        res = cur.execute("SELECT * FROM todos")
        print(res.fetchall())
    elif a == 5:
        res = cur.execute("SELECT * FROM todos")
        print(res.fetchall())
        x1 = str(input("Enter an item: "))
        x = str(input("Make Changes:  "))
        cur.execute("UPDATE todos SET item=? WHERE id=?", (x1, x))
        con.commit()
        res = cur.execute("SELECT * FROM todos")
        print(res.fetchall())
    elif a == 6:
        break