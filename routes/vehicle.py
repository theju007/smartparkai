from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from extensions import db
from models.vehicle import Vehicle

vehicle = Blueprint("vehicle", __name__)


@vehicle.route("/vehicles")
@login_required
def my_vehicles():

    vehicles = Vehicle.query.filter_by(user_id=current_user.id).all()

    return render_template(
        "user/my_vehicles.html",
        vehicles=vehicles
    )

#----------------Add--------------
@vehicle.route("/vehicles/add", methods=["GET", "POST"])
@login_required
def add_vehicle():

    if request.method == "POST":

        new_vehicle = Vehicle(

            user_id=current_user.id,

            vehicle_number=request.form["vehicle_number"],

            vehicle_type=request.form["vehicle_type"],

            brand=request.form["brand"],

            model=request.form["model"],

            color=request.form["color"]

        )

        db.session.add(new_vehicle)

        db.session.commit()

        flash("Vehicle Added Successfully!", "success")

        return redirect(url_for("vehicle.my_vehicles"))

    return render_template("user/add_vehicle.html")
#------------Edit--------------------
@vehicle.route("/vehicles/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_vehicle(id):

    vehicle_obj = Vehicle.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    if request.method == "POST":

        vehicle_obj.vehicle_number = request.form["vehicle_number"]
        vehicle_obj.vehicle_type = request.form["vehicle_type"]
        vehicle_obj.brand = request.form["brand"]
        vehicle_obj.model = request.form["model"]
        vehicle_obj.color = request.form["color"]

        db.session.commit()

        flash("Vehicle Updated Successfully!", "success")

        return redirect(url_for("vehicle.my_vehicles"))

    return render_template(
        "user/edit_vehicle.html",
        vehicle=vehicle_obj
    )
#---------Delete--------------
@vehicle.route("/vehicles/delete/<int:id>")
@login_required
def delete_vehicle(id):

    vehicle_obj = Vehicle.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(vehicle_obj)
    db.session.commit()

    flash("Vehicle Deleted Successfully!", "success")

    return redirect(url_for("vehicle.my_vehicles"))