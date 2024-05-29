import pymongo
from pymongo import MongoClient

if __name__ == '__main__':
    """ 
    1. connection to the MongoDB server
    2. create or connect to a database
    3. create or connect to a collection
    4. insert a document into the collection
    5. find a document in the collection
    6. update a document in the collection
    7. delete a document from the collection
    8. close the connection
    """
    client = MongoClient('localhost', 27017) 
    db = client["ukkwDB"]

    # Create or connect to a collection
    user_col = db["users"]
    course_col = db['siwp2005']

    # Insert a document into the collection
    user_doc = {"user_id": 1, "username": "test_user", "password": "some_password", "name": "Monica", "age": 20, "city": "Jakarta"}
    user_col.insert_one(user_doc)

    # Find a document in the collection
    found_document = user_col.find_one({"username": "test_user"})
    print(found_document)

    # Update a document in the collection
    user_col.update_one({"username": "test_user"}, {"$set": {"age": 21, "city": "Bandung", 'name': 'Jesica'}})

    # Delete a document from the collection
    user_col.delete_one({"username": "test_user"})

    # Close the connection
    client.close()
