from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)


if __name__ == '__main__':
    # mongodb
    client = MongoClient('localhost', 27017)

    db = client.flask_db
    collection_user = db.users
    
    # app.run(debug=True)
    app.run(host='0.0.0.0', port = 5002,  debug=True)

