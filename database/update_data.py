import sqlite3

conn = sqlite3.connect("todo.db")
c = conn.cursor()

rows = c.execute("SELECT * FROM tasks")
for row in rows:
    print(row)
print()

c.execute("UPDATE tasks SET priority = ? WHERE id = ?", (20, 1))
conn.commit()

rows = c.execute("SELECT * FROM tasks")
for row in rows:
    print(row)

c.close()
