from flask import Blueprint, request, jsonify
from models.admin_model import verify_admin, create_admin_once

admin_auth = Blueprint("admin_auth", __name__)

# create default admin (only once)
create_admin_once()

@admin_auth.route("/admin/login", methods=["POST"])
def admin_login():
    data = request.json
    if verify_admin(data.get("username"), data.get("password")):
        return jsonify({"success": True})
    return jsonify({"success": False}), 401
