import os
import math
from datetime import datetime

from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required

from extensions import db
from models import booking
from models.booking import Booking
from models.parking_slot import ParkingSlot

exit_bp = Blueprint("exit", __name__)


@exit_bp.route("/exit/<int:booking_id>")
@login_required
def vehicle_exit(booking_id):

    booking = Booking.query.get_or_404(booking_id)

    # 1. Complete Booking
    booking.status = "Completed"

    # 2. Save actual exit time
    booking.exit_time = datetime.now()
    current_time = datetime.now()

    if current_time < booking.entry_time:
        flash(
            "Vehicle cannot exit before the booking start time.",
            "danger"
            )
        return redirect(url_for("my_bookings.my_bookings_page"))

    booking.exit_time = current_time
    # Calculate Parking Duration
    duration = booking.exit_time - booking.entry_time

    # Convert duration to hours
    hours = duration.total_seconds() / 3600

    # Parking Rate (₹30/hour)
    RATE_PER_HOUR = 30

    # Calculate Fee
    booking.parking_fee = math.ceil(hours) * 30
    # Debug Output
    print("=================================")
    print("Entry Time :", booking.entry_time)
    print("Exit Time  :", booking.exit_time)
    print("Hours      :", hours)
    print("Parking Fee:", booking.parking_fee)
    print("=================================")

    # 3. Free the parking slot
    slot = ParkingSlot.query.get(booking.slot_id)

    if slot:
        slot.status = "Available"

    # 4. Delete QR Image
    if booking.qr_filename:

        qr_path = os.path.join(
            "static",
            "qr_codes",
            booking.qr_filename
        )

        if os.path.exists(qr_path):
            os.remove(qr_path)

        booking.qr_filename = None

    db.session.commit()

    flash("Vehicle exited successfully!", "success")

    return redirect(
        url_for("my_bookings.my_bookings_page")
    )