from datetime import datetime

from extensions import db


class ParkingSlot(db.Model):

    __tablename__ = "parking_slots"

    id = db.Column(db.Integer, primary_key=True)

    slot_number = db.Column(db.String(10), unique=True, nullable=False)

    floor = db.Column(db.Integer, default=1)

    slot_type = db.Column(db.String(20), default="Car")

    status = db.Column(
        db.Enum("Available", "Reserved", "Occupied"),
        default="Available",
        nullable=False,
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)