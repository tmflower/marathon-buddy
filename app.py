from flask import Flask,render_template, redirect, flash, session, request, jsonify
from models import db, connect_db, User, Week, Day
from flask_debugtoolbar import DebugToolbarExtension
import requests, json, os, re

app = Flask(__name__)

uri = os.environ.get('DATABASE_URL', 'postgresql:///marathon-buddy')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mochi')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """Displays landing page."""
    return render_template('home.html')


#  Probably don't need this route at all
@app.route('/users')
def show_users():
    """Displays list of all users"""
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/num-weeks-form', methods= ["GET", "POST"])
def show_num_weeks_form():
    """Shows form  & allows user to enter training period"""
    if request.method == "POST":
        num_weeks = request.form.get('num_weeks')
        
        # user and week will be identified by login and session (do this later)

        user = User.query.get(2)
        user.num_weeks = num_weeks
        db.session.add(user)
        db.session.commit()
        weeks = list(range(1, user.num_weeks + 1))
        session['weeks'] = weeks
        return redirect('/weekly-miles-form')
    return render_template('num_weeks_form.html')

@app.route('/weekly-miles-form', methods= ["GET", "POST"])
def show_weekly_mileage_form():
    """Shows form  & allows user to enter mileage goals per week"""
    
    # user and week will be identified by login and session (do this later)
    
    user = User.query.get(2)
    weeks = session['weeks']

    if request.method == "POST":
        weekly_miles = request.form.to_dict()
        # print(weekly_miles)
        for (week, weekly_miles) in weekly_miles.items():
            # print('On week', week ,'you will run', weekly_miles, 'miles')
            week = Week(num=week, mileage_target=weekly_miles, user=user.id)
            db.session.add(week)
            db.session.commit()
        return redirect('/daily-miles-form')          

    return render_template('weekly_miles_form.html', weeks=weeks, num_weeks=user.num_weeks)

@app.route('/daily-miles-form', methods=["GET", "POST"])
def show_daily_mileage_form():
    """Shows form & allows user to enter mileage goals per day"""
    
    # user and week will be identified by login and session (do this later)

    user = User.query.get(2)
    week = Week.query.get(8)

    one_week = list(range(1,8))
    if request.method == "POST":
        print(request.form)
        daily_miles = request.form.to_dict()
        print(daily_miles)
        for (day, daily_miles) in daily_miles.items():
            print('On day', day ,'you will run', daily_miles, 'miles')
            day = Day(num=day, mileage_target=daily_miles, week=week.num, user=user.id)
            db.session.add(day)
            db.session.commit()
        return redirect('/,y-training-plan') 
    return render_template('daily_miles_form.html', one_week=one_week, week=week.num)

@app.route('/my-training-plan')
def show_plan():
    """Displays plan and allows user to mark off miles as completed"""

    # user and week will be identified by login and session (do this later)
    # currently lists everything in display; will fix this later to have dropdowns for each week, or whatever options for displaying more details vs. less

    user = User.query.get(1)
    week = Week.query.get(5)

    my_weeks = Week.query.filter(Week.user == user.id).all()
    my_days = Day.query.filter(Day.user == user.id).all()
    print(my_days[0].week)
    print(week.id)

    return render_template('my_training_plan.html', user=user, week=week.num, my_weeks=my_weeks, my_days=my_days)

@app.route('/weekly-view/<int:week>')
def show_week(week):
    """Displays plan details for single week"""

    # user and week will be identified by login and session (do this later)
    user = User.query.get(1)
    week = Week.query.get(1)
    my_days = Day.query.filter(Day.week == week.num, Day.user == user.id).all()

    return render_template('weekly_details.html', user=user, week=week, my_days=my_days)