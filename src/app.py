from flask import Flask, Blueprint
from src.models import db
from .config import app_config
from .views.user_view import user_api as user_blueprint
from .views.wish_view import wish_api as wish_blueprint



def create_app(env_name):

    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(app_config[env_name])
    app.register_blueprint(user_blueprint, url_prefix='/api/')
    app.register_blueprint(wish_blueprint, url_prefix='/api/')

    @app.route('/', methods=['GET'])
    def index():

        return 'api is working'



    return app