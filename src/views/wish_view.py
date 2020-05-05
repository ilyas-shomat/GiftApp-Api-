from flask import request, json, Response, Blueprint, jsonify
from src.models.wish_model import Wish

wish_api = Blueprint('wishes', __name__)

"""
Get all wish list
"""
@wish_api.route('/wishes/', methods=['GET'])
def get_all_wishes():

    wishes = Wish.get_all_wishes()
    output_data = []

    for wish in wishes:
        wish_data = {}
        wish_data['wish_id'] = wish.id
        wish_data['wish_text'] = wish.text
        wish_data['wish_like'] = wish.like
        wish_data['wish_date'] = wish.date
        wish_data['wish_user_id'] = wish.user_id
        output_data.append(wish_data)

    return jsonify({'wishes': output_data})

"""
Get one wish in list
"""
@wish_api.route('/wishes/<id>/', methods=['GET'])
def get_one_wish(id):

    wish = Wish.get_wish_by_id(id)

    if not wish:
        return jsonify({'message': 'Wish not found'})

    wish_data = {}
    wish_data['wish_id'] = wish.id
    wish_data['wish_text'] = wish.text
    wish_data['wish_like'] = wish.like
    wish_data['wish_date'] = wish.date
    wish_data['wish_user_id'] = wish.user_id

    return jsonify({'wishes': wish_data})

"""
Create new wish 
"""
@wish_api.route('/wishes/', methods=['POST'])
def create_new_wish():

    data = request.get_json()

    new_wish = Wish(
        text=data['text'],
        like=False,
        date="",
    )

    new_wish.add_wish()
    return jsonify({'message': 'successfully added'})

"""
Edit one wish in list
"""
@wish_api.route('/wishes/<id>', methods=['PUT'])
def edit_one_wish(id):

    data = request.get_json()
    wish = Wish.get_wish_by_id(id)

    if not wish:
        return jsonify({'message': 'Wish not found'})

    wish.update_wish_data(data=data)
    return jsonify({'message': 'Wish data is updated'})


@wish_api.route('/wishes/<id>', methods=['DELETE'])
def delete_wish(id):

    wish = Wish.get_wish_by_id(id)

    if not wish:
        return jsonify({'message': 'Wish not found'})

    wish.delete_wish()

    return jsonify({'message': "Wish deleted"})