"""
Exercise 2: Inventory System
Build an inventory system with:
- Product table (name, price, quantity)
- Daily sales tracking table
- Low stock alerts
(Use sqlite3. Simulate DB and alerts if needed.)
"""

import sqlite3
from datetime import datetime

class InventorySystem:
    def __init__(self, db_file='inventory.db'):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()
    def create_tables(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            quantity INTEGER
        )''')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            date TEXT,
            quantity INTEGER,
            FOREIGN KEY(product_id) REFERENCES products(id)
        )''')
        self.conn.commit()
    def add_product(self, name, price, quantity):
        self.conn.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
        self.conn.commit()
    def record_sale(self, product_name, quantity):
        cur = self.conn.cursor()
        cur.execute('SELECT id, quantity FROM products WHERE name=?', (product_name,))
        row = cur.fetchone()
        if not row:
            print(f'Product {product_name} not found.')
            return
        pid, stock = row
        if stock < quantity:
            print(f'Not enough stock for {product_name}.')
            return
        self.conn.execute('UPDATE products SET quantity=quantity-? WHERE id=?', (quantity, pid))
        self.conn.execute('INSERT INTO sales (product_id, date, quantity) VALUES (?, ?, ?)', (pid, datetime.now().strftime('%Y-%m-%d'), quantity))
        self.conn.commit()
        print(f'Sale recorded for {product_name}: {quantity} units.')
        self.check_low_stock(pid)
    def check_low_stock(self, pid, threshold=5):
        cur = self.conn.cursor()
        cur.execute('SELECT name, quantity FROM products WHERE id=?', (pid,))
        name, qty = cur.fetchone()
        if qty < threshold:
            print(f'ALERT: Low stock for {name} ({qty} left)!')
    def close(self):
        self.conn.close()

def main():
    print('=== Inventory System ===')
    inv = InventorySystem(':memory:')
    inv.add_product('Widget', 9.99, 10)
    inv.add_product('Gadget', 14.99, 3)
    inv.record_sale('Widget', 2)
    inv.record_sale('Gadget', 2)
    inv.record_sale('Gadget', 1)
    inv.close()

if __name__ == '__main__':
    main() 