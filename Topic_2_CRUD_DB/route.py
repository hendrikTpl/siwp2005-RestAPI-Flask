from flask import request, jsonify
from db import get_users, get_user_by_id, insert_user, update_user, delete_user

def register_routes(app):
    @app.route('/api/users', methods=['GET'])
    def api_get_users():
        return jsonify(get_users())

    @app.route('/api/users/<user_id>', methods=['GET'])
    def api_get_user(user_id):
        return jsonify(get_user_by_id(user_id))

    @app.route('/api/users/add', methods=['POST'])
    def api_add_user():
        user = request.get_json()
        return jsonify(insert_user(user))

    @app.route('/api/users/update', methods=['PUT'])
    def api_update_user():
        user = request.get_json()
        return jsonify(update_user(user))

    @app.route('/api/users/delete/<user_id>', methods=['DELETE'])
    def api_delete_user(user_id):
        return jsonify(delete_user(user_id))
