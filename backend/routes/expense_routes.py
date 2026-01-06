from flask import Blueprint, request, jsonify
from database import db
from datetime import datetime

expense = Blueprint("expense", __name__)
expenses_collection = db["expenses"]

@expense.route("/admin/expense/add", methods=["POST"])
def add_expense():
    data = request.json

    expense_data = {
        "title": data.get("title"),
        "amount": data.get("amount"),
        "year": data.get("year"),
        "date": datetime.now()
    }

    expenses_collection.insert_one(expense_data)
    return jsonify({"message": "Expense added successfully"})
