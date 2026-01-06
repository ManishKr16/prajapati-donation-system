from database import db
from datetime import datetime

donations = db.donations

def add_donation(name, amount):
    donations.insert_one({
        "name": name,
        "amount": int(amount),
        "date": datetime.now(),
        "year": datetime.now().year
    })

def get_donations_by_year(year):
    return list(donations.find(
        {"year": year},
        {"_id": 0}
    ))

def get_total_by_year(year):
    pipeline = [
        {"$match": {"year": year}},
        {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
    ]
    result = list(donations.aggregate(pipeline))
    return result[0]["total"] if result else 0
