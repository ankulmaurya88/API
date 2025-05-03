# from .models import User
# from .database import db

from database import db
from models import User
# from schemas import UserSchema
# from routers.user import user_bp

# Create a user
def create_user(name: str, email: str):
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user

# Get all users
def get_users():
    return User.query.all()

# Get a user by ID
def get_user(user_id: int):
    return User.query.get(user_id)
