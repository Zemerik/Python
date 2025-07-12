"""
Exercise 1: Contact Manager
Create a contact manager that:
- Stores name/email/phone in SQLite
- Allows search by name/phone
- Exports contacts to CSV
(Use sqlite3 and pandas. Simulate DB and CSV if needed.)
"""

import sqlite3
import pandas as pd
import os

class ContactManager:
    def __init__(self, db_file='contacts.db'):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.create_table()
    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT
        )''')
        self.conn.commit()
    def add_contact(self, name, email, phone):
        self.conn.execute('INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
        self.conn.commit()
    def search(self, keyword):
        cur = self.conn.cursor()
        cur.execute('SELECT name, email, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?', (f'%{keyword}%', f'%{keyword}%'))
        return cur.fetchall()
    def export_csv(self, out_file='contacts_export.csv'):
        df = pd.read_sql_query('SELECT name, email, phone FROM contacts', self.conn)
        df.to_csv(out_file, index=False)
        print(f'Contacts exported to {out_file}')
    def close(self):
        self.conn.close()

def main():
    print('=== Contact Manager ===')
    mgr = ContactManager(':memory:')  # Use in-memory DB for demo
    mgr.add_contact('Alice', 'alice@example.com', '123-456-7890')
    mgr.add_contact('Bob', 'bob@example.com', '555-123-4567')
    mgr.add_contact('Carol', 'carol@example.com', '987-654-3210')
    print('Search results for "123":', mgr.search('123'))
    mgr.export_csv('contacts_export.csv')
    mgr.close()

if __name__ == '__main__':
    main() 