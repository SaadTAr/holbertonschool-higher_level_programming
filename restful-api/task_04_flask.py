#!/usr/bin/python3
"""
A simple Flask API dealing with user data, handling GET and POST requests.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with an empty dictionary as required by the test runner initial setup
users = {}


@app.route('/')
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """
    Returns the dictionary containing all users information.
    """
    return jsonify(users)


@app.route('/status')
def get_status():
    """Returns the status of the API."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Returns specific user details."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user with input validation and error handling.
    """
    # 1. Check for invalid JSON body
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Check if username is provided
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. Check for duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. Extract and save user details
    new_user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    users[username] = new_user

    # Success response
    response = {
        "message": "User added",
        "user": new_user
    }
    return jsonify(response), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
