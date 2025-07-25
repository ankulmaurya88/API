from flask import request, jsonify
from ..models.user import get_user_by_username
from ..services.jwt_service import create_jwt_token

def login():
    data = request.get_json()
    user = get_user_by_username(data.get("username"))

    if user and user["password"] == data.get("password"):
        token = create_jwt_token(user["user_id"], user["username"])
        return jsonify({"token": token})
    
    return jsonify({"message": "Invalid credentials"}), 401
