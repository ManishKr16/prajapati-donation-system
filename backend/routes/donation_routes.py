from flask import Blueprint, request, jsonify
from models.donation import add_donation

donation = Blueprint("donation", __name__)

@donation.route("/donate", methods=["POST"])
def donate():
    data = request.json

    user_id = data.get("user_id")
    amount = data.get("amount")

    if not user_id or not amount:
        return jsonify({"message": "Invalid data"}), 400

    add_donation(user_id, amount)
    return jsonify({"message": "Donation saved successfully"})
