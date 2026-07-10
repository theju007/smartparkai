from extensions import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    slot_id = db.Column(db.Integer, db.ForeignKey("parking_slots.id"))

    booking_date = db.Column(db.Date)

    entry_time = db.Column(db.DateTime)

    exit_time = db.Column(db.DateTime)

    status = db.Column(
        db.Enum("Booked", "Cancelled", "Completed"),
        default="Booked"
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)