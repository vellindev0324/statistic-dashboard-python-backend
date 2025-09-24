from flask import Flask
from flask_cors import CORS  # Import CORS
from .routes import register_routes, recording_daily_data


def create_app():
    app = Flask(__name__)

    # load config
    app.config.from_object("app.config.Config")

    # register blueprints/routes
    register_routes(app)


    return app
    
