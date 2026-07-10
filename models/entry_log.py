from extensions import db
from datetime import datetime

class EntryLog(db.Model):
    __tablename__ = "entry_logs"

    id = db.Column(db.Integer, primary_key=True)

    vehicle_number = db.Column(db.String(20))

    slot_number = db.Column(db.String(10))

    entry_time = db.Column(db.DateTime, default=datetime.utcnow)