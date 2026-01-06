from flask import Blueprint, request, jsonify
from models.user_model import create_user, login_user

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.json
    create_user(data)
    return jsonify({"message": "User registered successfully"})

@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    user = login_user(data)

    if user:
        return jsonify(user)
    return jsonify({"message": "Invalid credentials"}), 401
