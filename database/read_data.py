import sqlite3

conn = sqlite3.connect("todo.db")
c = conn.cursor()

# execute returns iterable cursor object
rows = c.execute("SELECT * FROM tasks")
print(type(rows))
for row in rows:
    print(row)

c.execute("SELECT * FROM tasks")
# fetchall returns data object
rows = c.fetchall()
print(type(rows))
for row in rows:
    print(row)

conn.close()
