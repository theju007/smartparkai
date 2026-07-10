from flask import Flask

from config import Config
from extensions import db, bcrypt, login_manager

# Import models so SQLAlchemy knows about them
from models.user import User
from models.parking_slot import ParkingSlot
from models.vehicle import Vehicle
from models.booking import Booking
from models.entry_log import EntryLog
from models.exit_log import ExitLog

# Import blueprint
from routes.auth import auth


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    return app


app = create_app()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == "__main__":
    app.run(debug=True)