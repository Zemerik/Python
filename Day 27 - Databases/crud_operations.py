import sqlite3

class UserManager:
    def __init__(self, db_name='users.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            age INTEGER)''')
        self.conn.commit()

    def add_user(self, name, age):
        self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)",
                          (name, age))
        self.conn.commit()

    def get_users(self):
        return self.cursor.execute("SELECT * FROM users").fetchall()

    def __del__(self):
        self.conn.close()

# Usage
manager = UserManager()
manager.add_user("Bob", 30)
print("All users:", manager.get_users())