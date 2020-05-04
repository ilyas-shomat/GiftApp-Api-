from flask import Flask
from src.models import db
from .config import app_config


def create_app(env_name):

    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(app_config[env_name])

    @app.route('/', methods=['GET'])
    def index():

        return 'api is working'

    return app