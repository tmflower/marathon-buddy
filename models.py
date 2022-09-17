from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


#####################################################################
###     
###     Which should have unique constraint?
#####################################################################
class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    total_miles_completed = db.Column(db.Float, default=0)
    num_weeks = db.Column(db.Integer, default=16)

    @classmethod
    def register(cls, username, password):
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        return cls(username=username, password=hashed_utf8)

    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False

class Week(db.Model):

    __tablename__ = "weeks"

    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    mileage_target = db.Column(db.Float, default=0)
    miles_completed = db.Column(db.Float, default=0)
    user = db.Column(db.ForeignKey('users.id', ondelete='cascade'))

class Day(db.Model):

    __tablename__ = "days"

    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    mileage_target = db.Column(db.Float, default=0)
    miles_completed = db.Column(db.Float, default=0)
    week = db.Column(db.Integer, db.ForeignKey('weeks.id', ondelete='cascade'))
    user = db.Column(db.ForeignKey('users.id', ondelete='cascade'))