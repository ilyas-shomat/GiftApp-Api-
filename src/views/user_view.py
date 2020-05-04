from flask import request, json, Response, Blueprint, jsonify
import uuid
from src.models.user_model import User

user_api = Blueprint('users', __name__)

"""
Create User Function
"""
@user_api.route('/users/', methods=['POST'])
def create_user():

    data = request.get_json()

    # check if user already exist in the db
    user_in_db = User.get_user_by_name(data.get('name'))
    if user_in_db:
        return jsonify({'message': 'User already exist'})

    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], appealName=data['appeal_name'], password=data['password'])
    new_user.add_user()

    return jsonify({'message': 'success'})


@user_api.route('/users/', methods=['GET'])
def get_all_user():

    users = User.get_all_users()
    output_data = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['appeal_name'] = user.appealName
        user_data['password'] = user.password

    return jsonify({'users': output_data})