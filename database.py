import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            image_filename TEXT
        )
    ''')
    conn.execute('''
      CREATE TABLE IF NOT EXISTS cart_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password, email):
  conn = get_db_connection()
  password_hash = generate_password_hash(password)
  conn.execute("INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)",
  (username, password_hash, email))
  conn.commit()
  conn.close()

def get_user_by_username(username):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
  conn = get_db_connection()
  user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
  conn.close()
  return user

def verify_password(password, password_hash):
    return check_password_hash(password_hash, password)

def get_all_products():
  conn = get_db_connection()
  products = conn.execute("SELECT * FROM products").fetchall()
  conn.close()
  return products

def get_product_by_id(product_id):
    conn = get_db_connection()
    product = conn.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
    conn.close()
    return product

def add_item_to_cart(user_id, product_id, quantity):
    conn = get_db_connection()
    conn.execute("INSERT INTO cart_items (user_id, product_id, quantity) VALUES (?, ?, ?)",
                  (user_id, product_id, quantity))
    conn.commit()
    conn.close()

def get_cart_items_by_user(user_id):
    conn = get_db_connection()
    cart_items = conn.execute(
        "SELECT cart_items.id as cart_item_id, products.*, cart_items.quantity FROM cart_items "
        "JOIN products ON cart_items.product_id = products.id "
        "WHERE cart_items.user_id = ?", (user_id,)).fetchall()
    conn.close()
    return cart_items

def update_cart_item_quantity(cart_item_id, quantity):
   conn = get_db_connection()
   conn.execute("UPDATE cart_items SET quantity = ? WHERE id = ?", (quantity, cart_item_id))
   conn.commit()
   conn.close()

def remove_cart_item(cart_item_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM cart_items WHERE id = ?", (cart_item_id,))
    conn.commit()
    conn.close()

def add_products_test():
    conn = get_db_connection()
    products = [
       ("F_ROD_45", "Fucile oleopneumatico per pesca in apnea", 169.99, "F_ROD_45 (1).jpg"),
        ("SubSuit", "Muta da sub professionale", 249.99, "SubSuit (4).jpg"),
        ("Pinne belly", "Pinne per pesca a fondo", 99.99, "Pinne belly (4).jpg"),
        ("Contenitore da pesca", "Contenitore da pesca", 59.99, "Contenitore_da_pesca (1).jpg"),
         ("F_ROD_35", "Set Ledgering", 59.99, "F_ROD_35 (4).jpg"),
        ("Guadino da pesca", "Rete da pesca", 60.99, "Guadino_da_pesca (4).jpg"),
        ("MORAN", "Yacht", 900000.00, "Moran (4).jpg"),
         ("Acqua Spectra", "Attrezzatura completa per snorkeling e immersioni", 399.99, "AcquaSpectra (1).jpg"),
        ("MORAN FIVE", "Yacht", 5926000.00, "Moran_five (2).jpg"),
        ("Rot/5047", "Canna da pesca", 79.99, "Rot_50_47 (1).jpg"),
        ("Sacca da pesca", "Sacca da pesca", 49.99, "Sacca_da_pesca (4).jpg"),
        ("Sedia pieghevole da pesca", "Sedia pieghevole da pesca", 40.99, "Sedia_pieghevole_da_pesca (1).jpg"),
        ("Stivali", "Stivali da pesca", 35.00, "Stivali (2).jpg"),
        ("SubSuit2", "Muta da sub professionale avanzata", 349.99, "SubSuit2 (2).jpg")
    ]
    conn.executemany("INSERT INTO products (name, description, price, image_filename) VALUES (?, ?, ?, ?)", products)
    conn.commit()
    conn.close()

def get_product_by_name(product_name):
    conn = get_db_connection()
    product = conn.execute("SELECT * FROM products WHERE name = ?", (product_name,)).fetchone()
    conn.close()
    return product

def clear_products():
    conn = get_db_connection()
    conn.execute("DELETE FROM products")
    conn.commit()
    conn.close()

init_db()