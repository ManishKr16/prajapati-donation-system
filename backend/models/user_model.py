from database import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

users_collection = db["users"]

def create_user(data):
    user = {
        "user_id": str(uuid.uuid4()),
        "name": data.get("name"),
        "mobile": data.get("mobile"),
        "password": generate_password_hash(data.get("password"))
    }
    users_collection.insert_one(user)
    return user

def login_user(data):
    user = users_collection.find_one({"mobile": data.get("mobile")})

    if user and check_password_hash(user["password"], data.get("password")):
        return {
            "user_id": user["user_id"],
            "name": user["name"],
            "mobile": user["mobile"]
        }
    return None
