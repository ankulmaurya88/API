from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy object for database management
db = SQLAlchemy()
def init_db(app):
    db.init_app(app)