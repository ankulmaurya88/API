from flask import Flask
# from .database import db
from database import db

from routers.user import user_bp


# Initialize Flask app
app = Flask(__name__)

# MySQL Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/StudentManagement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disables Flask-SQLAlchemy event system

# Initialize SQLAlchemy
db.init_app(app)
# init_db(app)

with app.app_context():
    db.create_all()

# Register Blueprints for API routes
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
