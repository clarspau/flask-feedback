"""Models for the Flask-feedback."""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()


def connect_db(app):
    """
    Connect this database to the provided Flask app.
    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User Model."""

    __tablename__ = "users"

    username = db.Column(
        db.String(20),
        nullable=False,
        unique=True,
        primary_key=True
    )
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.column(db.String(30), nullable=False)
    last_name = db.column(db.String(30), nullable=False)
