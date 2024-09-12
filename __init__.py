from flask import *
from HIITTimer_routes import HIITTrackerAPI

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_BINDS'] = {
    'sqlite_db': 'sqlite:///local_db.sqlite3'
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(HIITTrackerAPI)

    return app