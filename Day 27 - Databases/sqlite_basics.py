import sqlite3

# Create database connection
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY, 
               name TEXT, 
               email TEXT)''')

# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
              ('Alice', 'alice@example.com'))

# Commit and close
conn.commit()
conn.close()