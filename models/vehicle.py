from datetime import datetime

from extensions import db


class Vehicle(db.Model):

    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    vehicle_number = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    vehicle_type = db.Column(
        db.String(20),
        nullable=False
    )

    brand = db.Column(
        db.String(50),
        nullable=False
    )

    model = db.Column(
        db.String(50),
        nullable=False
    )

    color = db.Column(
        db.String(30),
        nullable=False
    )

    rfid_uid = db.Column(
        db.String(100),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )