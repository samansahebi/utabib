from ..app import app
from flask import request, jsonify, Response
from .models import User
import json

# Creates new user
@app.route('/create-user', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    user = User(username=data['username'], name=data['name'], calls=data['calls']).save()
    return Response(jsonify(user.to_json()), status=200)

# Updates user by username
@app.route('/create-user/<str:username>', methods=['PUT'])
def update_user(username):
    data = json.loads(request.data)
    user = User.objects(username=username)
    if user:
        user.update(username=data['username'], name=data['name'], calls=data['calls']).save()
        return Response(jsonify(user.to_json()), status=200)
    else:
        return Response(jsonify({'error': 'user not found'}), status=404)

# Returns list of all users
@app.route('/list-users', methods=['GET'])
def list_users():
    user = User.objects().to_json()
    return jsonify(user)