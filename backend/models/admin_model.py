from database import db
from werkzeug.security import generate_password_hash, check_password_hash

admins = db.admins

def create_admin_once():
    if admins.count_documents({}) == 0:
        admins.insert_one({
            "username": "admin",
            "password": generate_password_hash("admin@151")
        })

def verify_admin(username, password):
    admin = admins.find_one({"username": username})
    if not admin:
        return False
    return check_password_hash(admin["password"], password)
