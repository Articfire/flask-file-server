# File: app.py
from flask import Flask
from config import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from blueprints import webapp_bp
    app.register_blueprint(webapp_bp)


app = create_app()

if __name__ == "__main__":
    app.run()