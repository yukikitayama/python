import sqlite3

conn = sqlite3.connect("todo.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);""")

# ? is query parameter that is replaced with the correct value during execution
c.execute("INSERT INTO tasks (name, priority) VALUES (?, ?)", ("My first task", 1))

# commit confirms the changes of the current transaction
# If not called, changes won't be visible in the database
conn.commit()
conn.close()
