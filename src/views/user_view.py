from flask import request, json, Response, Blueprint, jsonify
import uuid
from src.models.user_model import User
from src.shared.auth import Auth

user_api = Blueprint('users', __name__)

"""
Create User Function
"""
@user_api.route('/users/', methods=['POST'])
def create_user():

    data = request.get_json()

    user_in_db = User.get_user_by_name(data.get('name'))
    if user_in_db:
        return jsonify({'message': 'User already exist'})

    hashed_password = User.generate_hashed_password(data['password'])

    new_user = User(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        appealName=data['appeal_name'],
        password=hashed_password)
    new_user.add_user()

    return jsonify({'message': 'success'})

"""
Get all users list
"""
@user_api.route('/users/', methods=['GET'])
def get_all_user():

    users = User.get_all_users()
    output_data = []
    # print(users)

    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['appeal_name'] = user.appealName
        user_data['password'] = user.password
        output_data.append(user_data)

    return jsonify({'users': output_data})
"""
Get one list
"""
@user_api.route('/users/<id>/', methods=['GET'])
def get_one_user_by_Id(id):

    user = User.get_one_user(id)

    if not user:
        return jsonify({'message': 'User not found'})

    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['appeal_name'] = user.appealName
    user_data['password'] = user.password

    return jsonify({'user': user_data})

"""
Edit selected user's data
"""
@user_api.route('/users/<id>', methods=['PUT'])
def edit_user_data(id):

    data = request.get_json()
    user = User.get_one_user(id)

    if not user:
        return jsonify({'message': 'User not found'})

    user.update_user_info(data=data)
    return jsonify({'message': 'User data is updated'})

"""
Delete selected user
"""
@user_api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):

    user = User.get_one_user(id)

    if not user:
        return jsonify({'message': 'User not found'})

    user.delete_user()

    return jsonify({'message': "user deleted"})


@user_api.route('/users/login/', methods=['POST'])
def login():

    data = request.get_json()
    user_name = data['name']

    user = User.get_user_by_name(user_name)

    if not user:
        return jsonify({'message': 'No such user'})

    if not user.check_hashed_password(data['password']):
        return jsonify({'message': 'No such user'})

    token = Auth.generate_token(user.public_id)
    return jsonify({'token': token})
