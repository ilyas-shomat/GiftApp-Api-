from flask import Flask
from .config import app_config


def create_app(env_name):

    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    @app.route('/', methods=['GET'])
    def index():

        return 'api is working'

    return app