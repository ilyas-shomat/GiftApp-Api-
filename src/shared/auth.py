from functools import wraps
import jwt
from flask import json, Response, request, g
from src.config import Development
from ..models.user_model import User



class Auth():

  @staticmethod
  def generate_token(public_id):

    payload = {'sub': public_id}
    return jwt.encode(payload, Development.JWT_SECRET_KEY).decode("utf-8")


  def token_reuired(f):
    @wraps(f)
    def decorated(*args, **kwargs):
      token = None

      if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']

      if not token:
        return 'Token is missed!'

      try:
        data = jwt.decode(token, Development.JWT_SECRET_KEY)
        public_id = data['sub']
        current_user = User.query.filter_by(public_id=public_id).first()
      except:
        return 'Token is invalid!'

      return f(current_user, *args, **kwargs)

    return decorated