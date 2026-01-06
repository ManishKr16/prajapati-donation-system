from flask import Blueprint, Response
from database import db
import csv
from io import StringIO

report = Blueprint("report", __name__)

@report.route("/admin/report/csv/<int:year>")
def export_csv(year):
    donations = db["donations"].find({"year": year})

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Name", "Amount", "Date", "Year"])

    for d in donations:
        writer.writerow([
            d.get("name"),
            d.get("amount"),
            d.get("date"),
            d.get("year")
        ])

    output.seek(0)
    return Response(
        output,
        mimetype="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=donations_{year}.csv"
        }
    )
