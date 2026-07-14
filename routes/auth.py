from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from extensions import db, bcrypt
from models.user import User
from models.vehicle import Vehicle
from models.parking_slot import ParkingSlot
from models.booking import Booking
from models.user import User

auth = Blueprint("auth", __name__)


# ---------------- HOME ----------------

@auth.route("/")
def home():
    return render_template("index.html")


# ---------------- REGISTER ----------------

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check passwords
        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("auth.register"))

        # Check duplicate email
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered!", "warning")
            return redirect(url_for("auth.register"))

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = User(
            name=name,
            email=email,
            phone=phone,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful! Please login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


# ---------------- LOGIN ----------------

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):

            login_user(user)

            flash("Login Successful!", "success")

            return redirect(url_for("auth.dashboard"))

        flash("Invalid Email or Password", "danger")

    return render_template("auth/login.html")
#----------------- DASHBOARD ----------------
@auth.route("/dashboard")
@login_required
def dashboard():

    total_users = User.query.count()

    my_vehicles = Vehicle.query.filter_by(
        user_id=current_user.id
    ).count()

    available_slots = ParkingSlot.query.filter_by(
        status="Available"
    ).count()

    occupied_slots = ParkingSlot.query.filter_by(
        status="Occupied"
    ).count()

    reserved_slots = ParkingSlot.query.filter_by(
        status="Reserved"
    ).count()

    total_bookings = Booking.query.count()

    return render_template(

        "user/dashboard.html",

        total_users=total_users,

        my_vehicles=my_vehicles,

        available_slots=available_slots,

        occupied_slots=occupied_slots,

        reserved_slots=reserved_slots,

        total_bookings=total_bookings

    )
#---------------- LOGOUT ----------------
@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged out successfully.", "success")

    return redirect(url_for("auth.login"))
