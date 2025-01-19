from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)

app.config.from_object('config.Config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.models import User, Book

from app.routes import user_bp

app.register_blueprint(user_bp)

