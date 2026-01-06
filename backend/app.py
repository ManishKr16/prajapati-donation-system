
from routes.admin_auth_routes import admin_auth
from routes.expense_routes import expense
from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth
from routes.donation_routes import donation
from routes.admin_routes import admin
from routes.report_routes import report
from routes.report_pdf_routes import report_pdf




app = Flask(__name__)
CORS(app)

app.register_blueprint(expense)
app.register_blueprint(auth)
app.register_blueprint(donation)
app.register_blueprint(admin)
app.register_blueprint(admin_auth)
app.register_blueprint(report)
app.register_blueprint(report_pdf)



@app.route("/")
def home():
    return "Backend running successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

