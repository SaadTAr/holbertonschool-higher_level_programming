#!/usr/bin/env python3
"""Simple API using Python with Flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(list(users.values()))


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    new_user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    users[username] = new_user

    return jsonify({"message": "User added", "user": new_user}), 201


@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    del users[username]
    return jsonify({"message": "User deleted"}), 200


@app.route('/users/<username>/update', methods=['PUT'])
def update_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    user = users[username]
    for field in ('name', 'age', 'city'):
        if field in data:
            user[field] = data[field]

    return jsonify({"message": "User updated", "user": user}), 200


if __name__ == '__main__':
    app.run(debug=True)
