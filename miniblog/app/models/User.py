from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app import db
from sqlalchemy import Column, String

bcrypt = Bcrypt()


class User(db.Model):
    __tablename__ = 'users'
    id_user = db.Column('id_user', db.Integer, primary_key=True, autoincrement=True)

    username_user = db.Column('username_user', db.String(100), unique=True, nullable=False)
    email_user = db.Column('email_user', db.String(100), unique=True, nullable=False)
    password_hash = db.Column('password_user', db.String(255), nullable=False)  # Aumente para 255

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
