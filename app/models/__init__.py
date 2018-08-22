from flask_api import FlaskAPI
from instance.config import DevelopmentConfig
from app.models.StackOverflow import blue_print


def create_app(config):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(blue_print)

    return app