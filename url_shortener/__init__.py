from .config import Config


def create_app(config_class=Config):
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .models import db
    db.init_app(app)

    with app.app_context():
        from .shortener.routes import shortener
        from .errors.handlers import errors
        app.register_blueprint(shortener)
        app.register_blueprint(errors)

        return app
