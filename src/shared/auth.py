from functools import wraps
import jwt
from flask import json, Response, request, g
from ..models.user_model import User


class Auth():

  @staticmethod
  def generate_token(public_id):



    try:
      payload = {'sub': public_id
      }
      return jwt.encode(
        payload,
        'sisoft',
        'HS256'
      ).decode("utf-8")
    except Exception as e:
      return Response(
        mimetype="application/json",
        response=json.dumps({'error': 'error in generating user token'}),
        status=400
      )

  @staticmethod
  def decode_token(token):

    re = {'data': {}, 'error': {}}
    try:
      payload = jwt.decode(token, 'sisoft')
      re['data'] = {'user_id': payload['sub']}
      return re
    except jwt.ExpiredSignatureError as e1:
      re['error'] = {'message': 'token expired, please login again'}
      return re
    except jwt.InvalidTokenError:
      re['error'] = {'message': 'Invalid token, please try again with a new token'}
      return re