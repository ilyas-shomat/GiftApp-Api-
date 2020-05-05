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