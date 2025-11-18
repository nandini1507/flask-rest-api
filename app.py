from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST - create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "name": data["name"]}
    return jsonify(users[user_id]), 201

# PUT - update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    users[user_id].update(data)
    return jsonify(users[user_id]), 200

# DELETE - remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"deleted": deleted_user}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
