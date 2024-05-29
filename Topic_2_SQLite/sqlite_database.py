import sqlite3

def connect_to_db():
    return sqlite3.connect('example.db')

def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(name, email, age):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, email, age) VALUES (?, ?, ?)
    ''', (name, email, age))
    conn.commit()
    conn.close()

def get_users():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def get_user_by_id(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user(user_id, name, email, age):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?
    ''', (name, email, age, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
