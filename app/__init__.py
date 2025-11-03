from flask import Flask
from pymysql import connect
from app.extensions import db, ckeditor, login_manager
from app.config import Config
import os

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    create_database_if_not_exists(config_class)

    db.init_app(app)
    ckeditor.init_app(app)
    login_manager.init_app(app)

    from app.account.routes import account
    from app.dashboard.routes import dashboard
    from app.website.routes import website
    from app.error_handlers.routes import error_handler
    from config import Config
    from flask import current_app

    from app.models import user, posts, themes, contact, bookmarks, comments, stats

    app.register_blueprint(account)
    app.register_blueprint(dashboard)
    app.register_blueprint(website)
    app.register_blueprint(error_handler)

    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_SAMESITE='Lax'
    )

    @app.after_request
    def apply_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['Content-Security-Policy'] = "default-src 'self';"
        response.headers['Server'] = 'Hidden'
        return response

    @app.route('/test/')
    def test_page():
        return '<h1> Testing the App </h1>'

    ABS_PATH = os.path.dirname(__file__)
    REL_PATH = "static"

    STATIC_PATH = repr(str(app.config["STATIC_FOLDER"]))
    
    @app.route("/../static/<filename>")
    def static_path():
        pass

    return app


def create_database_if_not_exists(config):
    import re
    if not re.match(r'^[a-zA-Z0-9_]+$', config.DB_NAME):
        raise ValueError(f"Invalid database name: {config.DB_NAME}")
    
    conn = connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        port=config.DB_PORT,
        autocommit=True
    )
    cursor = conn.cursor()
    
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS %s CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
        (config.DB_NAME,)
    )
    cursor.close()
    conn.close()
