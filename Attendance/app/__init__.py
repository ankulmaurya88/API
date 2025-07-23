from flask import Flask
from app.extensions.db import db
# from app.extensions import db
from app.routes.routing import app_blueprint
from app.models import models  # Registers models

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(app_blueprint)

    return app


