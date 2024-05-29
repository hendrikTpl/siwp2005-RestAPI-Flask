import sqlite3

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''DROP TABLE IF EXISTS users''')
        conn.execute('''
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL
            );
        ''')
        conn.commit()
        print("User table created successfully")
    except Exception as e:
        print(f"User table creation failed: {e}")
    finally:
        conn.close()

def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)", 
                    (user['name'], user['email'], user['phone'], user['address'], user['country']))
        conn.commit()
        inserted_user = get_user_by_id(cur.lastrowid)
    except Exception as e:
        print(f"Failed to insert user: {e}")
        conn.rollback()
    finally:
        conn.close()

    return inserted_user

def get_users():
    users = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        for row in rows:
            user = {
                "user_id": row["user_id"],
                "name": row["name"],
                "email": row["email"],
                "phone": row["phone"],
                "address": row["address"],
                "country": row["country"]
            }
            users.append(user)
    except Exception as e:
        print(f"Failed to get users: {e}")
        users = []

    return users

def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        if row:
            user = {
                "user_id": row["user_id"],
                "name": row["name"],
                "email": row["email"],
                "phone": row["phone"],
                "address": row["address"],
                "country": row["country"]
            }
    except Exception as e:
        print(f"Failed to get user by id: {e}")
        user = {}

    return user

def update_user(user):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id = ?", 
                    (user["name"], user["email"], user["phone"], user["address"], user["country"], user["user_id"]))
        conn.commit()
        updated_user = get_user_by_id(user["user_id"])
    except Exception as e:
        print(f"Failed to update user: {e}")
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()

    return updated_user

def delete_user(user_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except Exception as e:
        print(f"Failed to delete user: {e}")
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message

# Initialize database with sample data
def initialize_db_with_sample_data():
    users = [
        {"name": "Charles Effiong", "email": "charles@gmail.com", "phone": "067765665656", "address": "Lui Str, Innsbruck", "country": "Austria"},
        {"name": "Sam Adebanjo", "email": "samadebanjo@gmail.com", "phone": "098765465", "address": "Sam Str, Vienna", "country": "Austria"},
        {"name": "John Doe", "email": "johndoe@gmail.com", "phone": "067765665656", "address": "John Str, Linz", "country": "Austria"},
        {"name": "Mary James", "email": "maryjames@gmail.com", "phone": "09878766676", "address": "AYZ Str, New York", "country": "United States"}
    ]

    create_db_table()
    for user in users:
        print(insert_user(user))

# Uncomment the line below to initialize the database with sample data
initialize_db_with_sample_data()
