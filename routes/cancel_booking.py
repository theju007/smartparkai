import os

from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required

from extensions import db
from models.booking import Booking
from models.parking_slot import ParkingSlot

cancel_booking = Blueprint(
    "cancel_booking",
    __name__
)


@cancel_booking.route("/cancel-booking/<int:booking_id>")
@login_required
def cancel(booking_id):

    booking = Booking.query.get_or_404(booking_id)

    # Already completed?
    if booking.status == "Completed":
        flash(
            "Completed booking cannot be cancelled.",
            "danger"
        )
        return redirect(
            url_for("my_bookings.my_bookings_page")
        )

    # Already cancelled?
    if booking.status == "Cancelled":
        flash(
            "Booking already cancelled.",
            "warning"
        )
        return redirect(
            url_for("my_bookings.my_bookings_page")
        )

    # Change booking status
    booking.status = "Cancelled"

    # Free parking slot
    slot = ParkingSlot.query.get(booking.slot_id)

    if slot:
        slot.status = "Available"

    # Delete QR Code
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

    flash(
        "Booking cancelled successfully.",
        "success"
    )

    return redirect(
        url_for("my_bookings.my_bookings_page")
    )