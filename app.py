from flask import Flask

from config import Config
from extensions import db, bcrypt, login_manager, migrate
from routes.vehicle import vehicle

# Import models so SQLAlchemy knows about them
from models.user import User
from models.parking_slot import ParkingSlot
from models.vehicle import Vehicle
from models.booking import Booking
from models.entry_log import EntryLog
from models.exit_log import ExitLog
from routes.parking import parking
from routes.booking import booking
from routes.my_bookings import my_bookings
from routes.cancel_booking import cancel_booking
from routes.payment import payment

# Import blueprint
from routes.auth import auth
from routes.exit import exit_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth)
    app.register_blueprint(vehicle)

   
    return app


app = create_app()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(parking)
app.register_blueprint(booking)
app.register_blueprint(my_bookings)
app.register_blueprint(exit_bp)
app.register_blueprint(cancel_booking)
app.register_blueprint(payment)

if __name__ == "__main__":
    app.run(debug=True)