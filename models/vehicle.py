from extensions import db

class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(100))
    vehicle_number = db.Column(db.String(20), unique=True)
    vehicle_type = db.Column(db.String(20))
    rfid_tag = db.Column(db.String(50), unique=True)