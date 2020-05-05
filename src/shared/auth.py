from functools import wraps
import jwt
from flask import json, Response, request, g
from src.config import Development
from ..models.user_model import User



class Auth():

  @staticmethod
  def generate_token(public_id):

    payload = {'sub': public_id}
    return jwt.encode(payload, Development.JWT_SECRET_KEY, 'HS256').decode("utf-8")


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