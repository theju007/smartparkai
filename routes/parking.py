from flask import Blueprint, render_template
from flask_login import login_required

from models.parking_slot import ParkingSlot

parking = Blueprint("parking", __name__)


@parking.route("/parking")

@parking.route("/parking")
@login_required
def parking_layout():

    slots = ParkingSlot.query.order_by(
        ParkingSlot.slot_number
    ).all()

    available = ParkingSlot.query.filter_by(
        status="Available"
    ).count()

    occupied = ParkingSlot.query.filter_by(
        status="Occupied"
    ).count()

    reserved = ParkingSlot.query.filter_by(
        status="Reserved"
    ).count()

    return render_template(
        "user/parking_layout.html",
        slots=slots,
        available=available,
        occupied=occupied,
        reserved=reserved
    )
