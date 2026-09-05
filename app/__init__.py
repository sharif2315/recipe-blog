import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_babel import lazy_gettext as _l, Babel
from app.database import db_session
from config import Config


def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"
login.login_message = _l('Please login to access this page')
babel = Babel()


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    babel.init_app(app, locale_selector=get_locale)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from . import auth
    app.register_blueprint(auth.bp, url_prefix='/auth')

    from .dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard') 
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app

from app import models