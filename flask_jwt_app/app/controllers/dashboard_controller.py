from flask import request, jsonify
from ..services.jwt_service import verify_jwt_token

def dashboard():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"message": "Missing token"}), 401

    try:
        token = auth_header.split(" ")[1]
        result = verify_jwt_token(token)

        if "error" in result:
            return jsonify({"message": result["error"]}), 401

        return jsonify({
            "message": "Welcome!",
            "user_id": result["user_id"],
            "username": result["username"]
        })

    except Exception:
        return jsonify({"message": "Token processing error"}), 400
