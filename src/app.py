from flask import Flask, Blueprint
from src.models import db
from .config import app_config
from .views.user_view import user_api as user_blueprint



def create_app(env_name):

    user = Blueprint('user', __name__)

    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(app_config[env_name])
    app.register_blueprint(user)
    app.register_blueprint(user_blueprint)

    @app.route('/', methods=['GET'])
    def index():

        return 'api is working'

    @user.route('/', methods=['GET'])
    def test():
        return 'work'

    return app