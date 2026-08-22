import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.database import db_session
from config import Config


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

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