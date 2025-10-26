import os
from dotenv import load_dotenv  # getting .env variables
from datetime import timedelta

class Config:
    DB_USER = os.environ['RDS_USERNAME']
    DB_PASSWORD =  os.environ['RDS_PASSWORD']
    DB_HOST = os.environ['RDS_HOSTNAME']
    DB_PORT = int(os.environ['RDS_PORT'])
    DB_NAME = os.environ['RDS_DB_NAME']
    SECRET_KEY = os.environ['SECRET_KEY']  # needed for login with wtforms
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True
    ABSOLUTE_PATH = os.path.dirname(__file__)
    RELATIVE_PATH = "static/Pictures_Users"
    BLOG_PICTURES_PATH = "static/Pictures_Posts"
    PROFILE_IMG_FOLDER = os.path.join(ABSOLUTE_PATH, RELATIVE_PATH)
    BLOG_IMG_FOLDER = os.path.join(ABSOLUTE_PATH, BLOG_PICTURES_PATH)
    STATIC_FOLDER = os.path.join(ABSOLUTE_PATH, "static")
    ALLOWED_IMG_EXTENSIONS = ['PNG', 'JPG', 'JPEG']
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

