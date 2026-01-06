from flask import Blueprint, jsonify, request
from models.donation import get_donations_by_year, get_total_by_year

admin = Blueprint("admin", __name__)

@admin.route("/admin/donations/year", methods=["GET"])
def donations_by_year():
    year = int(request.args.get("year"))

    donations = get_donations_by_year(year)
    total = get_total_by_year(year)

    return jsonify({
        "year": year,
        "total_amount": total,
        "donations": donations
    })
