import sqlite3

conn = sqlite3.connect('site.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
   
)
''')

conn.commit()   
conn.close()

print("Database and table created successfully.")