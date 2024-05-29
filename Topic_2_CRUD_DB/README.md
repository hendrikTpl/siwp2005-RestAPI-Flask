
# siwp2005-RestAPI-Flask

# [SIWP2005]_PBO_Building REST API with Flask

## CRUD and Connect to DB 

### NoSQL
- we will demonstrate mongoDB connection with flask
    - Quick introduction to NoSQL feel free to check [this video](https://www.youtube.com/watch?v=0buKQHokLK8) out 


### I) Installing MongoDB
> Overview

> For those of you who doesn't familiar with MongoDB feel free to check [this brief](https://www.youtube.com/watch?v=EE8ZTQxa0AM) introduction to MongoDB 

1. On Linux (Ubuntu)

* Import the MongoDB public GPG Key:
    check if `gnupg` and `curl` are available on ubuntu host, if not install it by this commands
`sudo apt-get install gnupg curl`

    MongoDB public GPG key
    ```
    curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
    ```

* Create a list file for MongoDB:
    - ubuntu 22.04
    ```
        echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
    ```
    
    - ubuntu 20.04
    ```
        echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
    ```


* Reload the local package database:

    ```bash
    sudo apt-get update
    ```
* Install the MongoDB packages:

    ```bash 
    sudo apt-get install -y mongodb-org
    ```

* Start MongoDB:

    ```bash
    sudo systemctl start mongod
    ```

* Enable MongoDB to start on system startup:

    ```
    sudo systemctl enable mongod
    ```

* Verify that MongoDB has started:

    ```bash
    sudo systemctl status mongod
    ```

2. On Windows

* Download MongoDB:

    Go to the [MongoDB Download Center](https://www.mongodb.com/try/download/community) and download the MongoDB Community Server for Windows.

* Run the MongoDB installer:

    Follow the installation wizard and choose the Complete setup.
    Make sure to select "Install MongoDB as a Service" during the     installation process.
    
* Set up the Data Directory:

    By default, MongoDB will use C:\Program Files\MongoDB\Server\7.0\data\db as the data directory. Ensure this directory exists.
    Verify the installation:

* Open Command Prompt and run:

```
mongod --version
```

* Start MongoDB:

    MongoDB should be running as a Windows service automatically. You can verify this by checking the services panel or by running:

```
net start MongoDB
```

### II) Using MongoDB with PyMongo
- Minimum example to use CRUD mechanism in MongoDB
```python
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

```

**References**
- https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/
- https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/
- https://www.w3schools.com/python/python_mongodb_insert.asp

### SQL
- Introduce an example to connect flask app with MySQL/Postgres





