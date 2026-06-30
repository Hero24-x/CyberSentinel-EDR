from flask import Flask

from app.core.config import Config
from app.core.extensions import (
    db,
    login_manager
)

def create_app():

    app = Flask(__name__)

    app.config.from_object(
        Config
    )

    db.init_app(app)
    login_manager.init_app(app)

    from app.api.dashboard import (
        dashboard_bp
    )

    app.register_blueprint(
        dashboard_bp
    )

    with app.app_context():
        db.create_all()

    return app
