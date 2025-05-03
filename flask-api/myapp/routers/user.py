from flask import Blueprint, request, jsonify
from flask.views import MethodView
# from ..crud import create_user, get_users, get_user
from crud import create_user, get_users, get_user

from schemas import UserCreate, UserOut
from pydantic import ValidationError

# Create Blueprint for user routes
user_bp = Blueprint('user', __name__)

class UserAPI(MethodView):

    # Method to handle GET requests for fetching all users or a specific user by ID
    def get(self, user_id=None):
        if user_id is None:
            # Get all users
            users = get_users()
            return jsonify([UserOut.from_orm(user).dict() for user in users])
        else:
            # Get user by ID
            user = get_user(user_id)
            if user is None:
                return jsonify({"error": "User not found"}), 404
            return jsonify(UserOut.from_orm(user).dict())

    # Method to handle POST requests for creating a new user
    def post(self):
        try:
            # Validate the incoming data with Pydantic
            user_data = UserCreate(**request.json)
        except ValidationError as e:
            return jsonify(e.errors()), 400

        # Create the user in the database
        user = create_user(name=user_data.name, email=user_data.email)
        return jsonify(UserOut.from_orm(user).dict()), 201

# Register the view for user routes
user_bp.add_url_rule('/users', view_func=UserAPI.as_view('users'), methods=['GET', 'POST'])
user_bp.add_url_rule('/users/<int:user_id>', view_func=UserAPI.as_view('user'), methods=['GET'])
