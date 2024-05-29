import pymongo
from pymongo import MongoClient

def connect_to_db():
    client = MongoClient('localhost', 27017)
    db = client["ukkwDB"]
    return db

def create_db_table():
    db = connect_to_db()
    db["users"].drop()
    print("User collection created successfully")

def insert_user(user):
    db = connect_to_db()
    user_col = db["users"]
    result = user_col.insert_one(user)
    return get_user_by_id(result.inserted_id)

def get_users():
    db = connect_to_db()
    user_col = db["users"]
    users = list(user_col.find())
    for user in users:
        user["_id"] = str(user["_id"])
    return users

def get_user_by_id(user_id):
    from bson import ObjectId
    db = connect_to_db()
    user_col = db["users"]
    user = user_col.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
    return user

def update_user(user):
    from bson import ObjectId
    db = connect_to_db()
    user_col = db["users"]
    result = user_col.update_one({"_id": ObjectId(user["_id"])}, {"$set": user})
    if result.modified_count > 0:
        return get_user_by_id(user["_id"])
    return {}

def delete_user(user_id):
    from bson import ObjectId
    db = connect_to_db()
    user_col = db["users"]
    result = user_col.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count > 0:
        return {"status": "User deleted successfully"}
    return {"status": "Cannot delete user"}

# Initialize database with sample data
def initialize_db_with_sample_data():
    users = [
        {"name": "Budi Santoso", "email": "budi.santoso@gmail.com", "phone": "081234567890", "address": "Jalan Sudirman, Jakarta", "country": "Indonesia"},
        {"name": "Siti Aminah", "email": "siti.aminah@gmail.com", "phone": "081234567891", "address": "Jalan Thamrin, Jakarta", "country": "Indonesia"},
        {"name": "Andi Wijaya", "email": "andi.wijaya@gmail.com", "phone": "081234567892", "address": "Jalan Gatot Subroto, Jakarta", "country": "Indonesia"},
        {"name": "Dewi Lestari", "email": "dewi.lestari@gmail.com", "phone": "081234567893", "address": "Jalan MH Thamrin, Jakarta", "country": "Indonesia"}
    ]

    create_db_table()
    for user in users:
        print(insert_user(user))

# Uncomment the line below to initialize the database with sample data
initialize_db_with_sample_data()
