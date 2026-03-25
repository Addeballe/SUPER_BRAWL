# https://docs.python.org/3/library/sqlite3.html
# sqlite3 is included in the Python standard library

import sqlite3

DB_FILE = "database.db"

try:
    cnx = sqlite3.connect(DB_FILE)
except sqlite3.Error as err:
    print(f"Failed to connect to database: {err}")
    raise SystemExit(1)

cursor = cnx.cursor()
query = ("SELECT Post.*, User.name as author FROM Post JOIN User ON Post.user_id = User.id")
cursor.execute(query)

for row in cursor:
    print(row)
    print(row[1], row[3])

cursor.close()
cnx.close()