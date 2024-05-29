from flask import Flask, request, jsonify
from flask_cors import CORS
from route import register_routes

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
register_routes(app)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5001, debug=True)
