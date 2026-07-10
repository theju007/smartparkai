from extensions import db
from datetime import datetime

class ExitLog(db.Model):
    __tablename__ = "exit_logs"

    id = db.Column(db.Integer, primary_key=True)

    vehicle_number = db.Column(db.String(20))

    slot_number = db.Column(db.String(10))

    exit_time = db.Column(db.DateTime, default=datetime.utcnow)

    parking_fee = db.Column(db.Float)