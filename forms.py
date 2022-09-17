from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import InputRequired, Length, NumberRange

class NewUserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(max=15, message="Username is too long! Keep it under 15 characters, please!")])
    password = StringField("Password", validators=[InputRequired(), Length(min=5, max=15, message="Password must be between 5 and 15 characters")])

class UserLoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(max=15)])
    password = StringField("Password", validators=[InputRequired(), Length(min=5, max=15)])

class NumWeeksForm(FlaskForm):
    num_weeks = IntegerField("Total number of weeks to train", validators=[InputRequired(), NumberRange(min=4, max=30, message="Number of weeks must be between 12 and 30")])

class WeeklyMilesForm(FlaskForm):
    weekly_miles = IntegerField("Total number of miles to run this week", validators=[InputRequired(), NumberRange(min=6, max=60, message="Number of miles for this week must be between 6 and 60")])

class DailyMilesForm(FlaskForm):
    daily_miles = DecimalField("Number of miles to run this day", validators=[InputRequired(), NumberRange(min=1, max=26.2, message="Number of miles must be between 1 and 26")])