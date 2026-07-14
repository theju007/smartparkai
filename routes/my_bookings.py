from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.booking import Booking

my_bookings = Blueprint("my_bookings", __name__)


@my_bookings.route("/my-bookings")
@login_required
def my_bookings_page():

    bookings = Booking.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Booking.id.desc()
    ).all()

    return render_template(
        "user/my_bookings.html",
        bookings=bookings
    )