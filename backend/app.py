from flask import Flask, send_from_directory
from flask_cors import CORS
import os

from routes.auth_routes import auth
from routes.donation_routes import donation
from routes.expense_routes import expense
from routes.admin_routes import admin
from routes.admin_auth_routes import admin_auth
from routes.report_routes import report
from routes.report_pdf_routes import report_pdf


app = Flask(__name__)
CORS(app)

# -------- Register Blueprints --------
app.register_blueprint(auth)
app.register_blueprint(donation)
app.register_blueprint(expense)
app.register_blueprint(admin)
app.register_blueprint(admin_auth)
app.register_blueprint(report)
app.register_blueprint(report_pdf)

# -------- Serve Frontend --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

@app.route("/")
def home():
    # Final public donation page
    return send_from_directory(FRONTEND_DIR, "donate.html")

@app.route("/admin-page")
def admin_page():
    return send_from_directory(FRONTEND_DIR, "admin.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)

# -------- Health Check --------
@app.route("/health")
def health():
    return {"status": "Backend running successfully"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
