import razorpay

from flask import (
    Blueprint,
    render_template,
    request,
    jsonify
)

from config import Config

payment = Blueprint(
    "payment",
    __name__
)

client = razorpay.Client(
    auth=(
        Config.RAZORPAY_KEY_ID,
        Config.RAZORPAY_KEY_SECRET
    )
)


@payment.route("/create-order", methods=["POST"])
def create_order():

    amount = int(request.form["amount"])

    order = client.order.create({

        "amount": amount * 100,

        "currency": "INR",

        "payment_capture": 1

    })

    return jsonify(order)