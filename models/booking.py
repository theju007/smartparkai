from datetime import datetime
from extensions import db


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    # Foreign Keys
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    slot_id = db.Column(
        db.Integer,
        db.ForeignKey("parking_slots.id"),
        nullable=False
    )

    # Relationship
    slot = db.relationship(
        "ParkingSlot",
        backref="bookings"
    )

    # Booking Details
    booking_date = db.Column(
        db.Date,
        nullable=False
    )

    entry_time = db.Column(
        db.DateTime,
        nullable=False
    )

    exit_time = db.Column(
        db.DateTime,
        nullable=False
    )

    # Booking Status
    status = db.Column(
        db.Enum("Booked", "Cancelled", "Completed"),
        default="Booked"
    )

    # QR Code Image Filename
    qr_filename = db.Column(
        db.String(255)
    )

    # Parking Fee
    parking_fee = db.Column(
        db.Float,
        default=0
    )
    payment_id = db.Column(db.String(150))

    payment_status = db.Column(
        db.Enum(
            "Pending",
            "Paid",
            "Failed",
            "Refunded"
        ),
        default="Pending"
    )

    payment_method = db.Column(
        db.String(50)
    )

    # Record Creation Time
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )