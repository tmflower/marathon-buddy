from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


#####################################################################
###    Should change ints to floats for partial miles!!!    ###
###     Which should have unique constraint? (week.num)
#####################################################################
class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    total_miles_completed = db.Column(db.Integer, default=0)
    num_weeks = db.Column(db.Integer, default=16)

class Week(db.Model):

    __tablename__ = "weeks"

    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    mileage_target = db.Column(db.Integer, default=0)
    miles_completed = db.Column(db.Integer, default=0)
    user = db.Column(db.ForeignKey('users.id', ondelete='cascade'))

class Day(db.Model):

    __tablename__ = "days"

    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    mileage_target = db.Column(db.Integer, default=0)
    miles_completed = db.Column(db.Integer, default=0)
    week = db.Column(db.Integer, db.ForeignKey('weeks.id', ondelete='cascade'))
    user = db.Column(db.ForeignKey('users.id', ondelete='cascade'))