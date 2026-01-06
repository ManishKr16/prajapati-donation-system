from flask import Blueprint, send_file
from database import db
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile

report_pdf = Blueprint("report_pdf", __name__)

@report_pdf.route("/admin/report/pdf/<int:year>")
def export_pdf(year):
    donations = list(db["donations"].find({"year": year}))

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(temp.name, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"Prajapati Club – Donation Report {year}")
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(50, y, "Name")
    c.drawString(200, y, "Amount")
    c.drawString(300, y, "Date")
    y -= 15

    total = 0
    for d in donations:
        if y < 50:
            c.showPage()
            y = height - 50

        c.drawString(50, y, str(d.get("name")))
        c.drawString(200, y, str(d.get("amount")))
        c.drawString(300, y, str(d.get("date")))
        total += int(d.get("amount", 0))
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Total Collection: ₹ {total}")

    c.save()
    return send_file(temp.name, as_attachment=True)
