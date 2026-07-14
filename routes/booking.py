from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime

from extensions import db
from models.booking import Booking
from models.parking_slot import ParkingSlot
from models.vehicle import Vehicle
import qrcode
import os

booking = Blueprint("booking", __name__)


@booking.route("/book/<int:slot_id>", methods=["GET", "POST"])
@login_required
def book_slot(slot_id):

    slot = ParkingSlot.query.get_or_404(slot_id)

    vehicles = Vehicle.query.filter_by(
        user_id=current_user.id
    ).all()

    if request.method == "POST":

        vehicle_id = request.form["vehicle_id"]

        entry_date = request.form["entry_date"]

        entry_time = request.form["entry_time"]

        exit_time = request.form["exit_time"]

        booking = Booking(

            user_id=current_user.id,

            slot_id=slot.id,

            booking_date=datetime.strptime(
                entry_date,
                "%Y-%m-%d"
            ).date(),

            entry_time=datetime.strptime(
                entry_date + " " + entry_time,
                "%Y-%m-%d %H:%M"
            ),

            exit_time=datetime.strptime(
                entry_date + " " + exit_time,
                "%Y-%m-%d %H:%M"
            ),

            status="Booked"

        )

        db.session.add(booking)

        # Update parking slot status
        slot.status = "Reserved"

        db.session.commit()
        # Generate QR Code

        qr_data = f"""
        Booking ID : {booking.id}
        User ID : {booking.user_id}
        Slot : {slot.slot_number}
        Status : {booking.status}
        """

        img = qrcode.make(qr_data)

        filename = f"booking_{booking.id}.png"

        filepath = os.path.join(
            "qr_codes",
        filename
        )

        img.save(filepath)

        flash(
            "Booking created successfully!",
            "success"
        )

        return redirect(url_for("auth.dashboard"))

    return render_template(
        "user/booking.html",
        slot=slot,
        vehicles=vehicles
    )