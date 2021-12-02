import sqlite3

conn = sqlite3.connect("users.db")

cur = conn.cursor()

cur.execute("SELECT cpr,password FROM users")

for detailList in cur:
    print(detailList[0], detailList[1])

conn.close()
