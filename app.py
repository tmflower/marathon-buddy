
from weakref import WeakValueDictionary
from flask import Flask,render_template, redirect, flash, session, request, jsonify
from models import db, connect_db, User, Week, Day
from flask_debugtoolbar import DebugToolbarExtension
import requests, json, os
from forms import NewUserForm, UserLoginForm, NumWeeksForm, WeeklyMilesForm, DailyMilesForm
from sqlalchemy.exc import IntegrityError
from starter_plan import setup_starter_plan

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

@app.route('/welcome')
def welcome():
    """Offers logged in user the option to set up plan or view plan"""

    # need to add a condition here: if user has plan, show both options; otherwise, only show setup option
    user_id = session['user_id']
    user = User.query.get(user_id)
    # if getPlanBtn.selected === True:

    return render_template('welcome.html', username=user.username)


@app.route('/register', methods= ["GET", "POST"])
def register():
    """Allows new user to sign up"""
    form = NewUserForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            password = form.password.data
            user = User.register(username, password)
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id

            flash(f"You have signed up, {username}!")
            return redirect('/welcome')

        except IntegrityError:
            flash("Sorry, that username is taken. Please try another")
            form.username.data = ""
            form.password.data = ""

    return render_template('register_form.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    """Allows registered user to login"""

    form = UserLoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)

        if user:
            session['user_id'] = user.id
            # flash(f"Welcome back, {username}!")
            return redirect('/welcome')
        else:
            flash("Sorry, your username or password is not valid. Please try again.")
            form.username.data = ""
            form.password.data = ""
    
    return render_template('login_form.html', form=form)

@app.route('/logout')
def logout():
    """Allows user to log out"""
    session.pop('user_id')
    return redirect('/')

@app.route('/starter-plan')
def get_starter_plan():
    """Applies default plan data for this user and redirects to training plan"""

    setup_starter_plan()
    # user_id = session['user_id']
    # user = User.query.get(user_id)

    # user.num_weeks = 16;

    # week1 = Week(num = 1, mileage_target = 19, user = user.id)
    # week2 = Week(num = 2, mileage_target = 21, user = user.id)
    # week3 = Week(num = 3, mileage_target = 25, user = user.id)
    # week4 = Week(num = 4, mileage_target = 23, user = user.id)
    # week5 = Week(num = 5, mileage_target = 30, user = user.id)
    # week6 = Week(num = 6, mileage_target = 32, user = user.id)
    # week7 = Week(num = 7, mileage_target = 28, user = user.id)
    # week8 = Week(num = 8, mileage_target = 35, user = user.id)
    # week9 = Week(num = 9, mileage_target = 39, user = user.id)
    # week10 = Week(num = 10, mileage_target = 35, user = user.id)
    # week11 = Week(num = 11, mileage_target = 41, user = user.id)
    # week12 = Week(num = 12, mileage_target = 31, user = user.id)
    # week13 = Week(num = 13, mileage_target = 42, user = user.id)
    # week14 = Week(num = 14, mileage_target = 30, user = user.id)
    # week15 = Week(num = 15, mileage_target = 23, user = user.id)
    # week16 = Week(num = 16, mileage_target = 34, user = user.id)
    # weeks = (week1, week2, week3, week4, week5, week6, week7, week8, week9, week10, week11, week12, week13, week14, week15, week16)
    # for week in weeks:
    #     db.session.add_all(week)
    #     db.session.commit()

    # day1 = Day(num=1, mileage_target=0, week=week1.id, user=user.id)
    # day2 = Day(num=2, mileage_target=3, week=week1.id, user=user.id)
    # day3 = Day(num=3, mileage_target=4, week=week1.id, user=user.id)
    # day4 = Day(num=4, mileage_target=0, week=week1.id, user=user.id)
    # day5 = Day(num=5, mileage_target=4, week=week1.id, user=user.id)
    # day6 = Day(num=6, mileage_target=0, week=week1.id, user=user.id)
    # day7 = Day(num=7, mileage_target=8, week=week1.id, user=user.id)
    # days = (day1, day2, day3, day4, day5, day6, day7)
    # for day in days:
    #     db.session.add(day)
    #     db.session.commit()

    # day1 = Day(num=1, mileage_target=0, week=week2.id, user=user.id)
    # day2 = Day(num=2, mileage_target=3, week=week2.id, user=user.id)
    # day3 = Day(num=3, mileage_target=4, week=week2.id, user=user.id)
    # day4 = Day(num=4, mileage_target=0, week=week2.id, user=user.id)
    # day5 = Day(num=5, mileage_target=4, week=week2.id, user=user.id)
    # day6 = Day(num=6, mileage_target=0, week=week2.id, user=user.id)
    # day7 = Day(num=7, mileage_target=10, week=week2.id, user=user.id)
    # days = (day1, day2, day3, day4, day5, day6, day7)
    # for day in days:
    #     db.session.add(day)
    #     db.session.commit()

    return redirect('/my-training-plan')
    

@app.route('/num-weeks-form', methods= ["GET", "POST"])
def show_num_weeks_form():
    """Shows form  & allows user to enter training period"""
    form = NumWeeksForm()

    if form.validate_on_submit():
        num_weeks = form.num_weeks.data

        user_id = session['user_id']
        user = User.query.get(user_id)
        user.num_weeks = num_weeks
        db.session.commit()

        """save this user's total number of weeks in session as a list & save week 1 as current week in session"""
        weeks = list(range(1, user.num_weeks + 1))
        session['weeks'] = weeks
        session['curr_week'] = 1
        return redirect('/weekly-miles-form')

    return render_template('num_weeks_form.html', form=form)


@app.route('/weekly-miles-form', methods= ["GET", "POST"])
def show_weekly_mileage_form():
    """Shows form  & allows user to enter mileage goals per week"""
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    curr_week = session['curr_week']

    form = WeeklyMilesForm()
    # default_miles = {1:19, 2:21, 3:25, 4:23}
    # for (week, weekly_miles) in default_miles.items:
    #     print(weekly_miles);
            # form.weekly_miles.data = weekly_miles

    if form.validate_on_submit():
              
        weekly_miles = form.weekly_miles.data
        
        """ create a new week for each number in this user's total number of weeks"""
        myWeek = Week(num=curr_week, mileage_target=weekly_miles, user=user.id, miles_completed=0)      
        db.session.add(myWeek)
        db.session.commit()
        session['curr_week'] = myWeek.num + 1
        if session['curr_week'] == user.num_weeks + 1:

            """ get this user's first week and save the id in session to access in other routes"""
            week1 = Week.query.filter(Week.user == user.id, Week.num == 1).first()
            session['week_id'] = week1.id
            return redirect('/my-training-plan')
        else:
            return render_template('weekly_miles_form.html', form=form, week=curr_week + 1, num_weeks=user.num_weeks)     

    return render_template('weekly_miles_form.html', form=form, week=curr_week, num_weeks=user.num_weeks)


@app.route('/daily-miles-form', methods=["GET", "POST"])
def show_daily_mileage_form():
    """Shows form & allows user to enter mileage goals per day """
    
    """ get current user and current week from session and db """
    user_id = session['user_id']
    user = User.query.get(user_id)
    curr_week = Week.query.filter(Week.user == user.id, Week.num == session['week_details']).first()

    """ create list of days to iterate through in template """
    one_week = list(range(1,8))

    """ create a day with user data for each day in this week for this user """ 
    if request.method == "POST":
        daily_miles = request.form.to_dict()
        for (day, daily_miles) in daily_miles.items():
            day = Day(num=day, mileage_target=daily_miles, miles_completed=0, week=curr_week.id, user=user.id)
            db.session.add(day)
            db.session.commit()
        return redirect('/my-training-plan')

    return render_template('daily_miles_form.html', one_week=one_week, curr_week=curr_week)
######################################################################################
## attempt to accomplish same result with WTForms, but only returns first value for all fields:
######################################################################################

    # form = DailyMilesForm() 
    # if form.validate_on_submit():
        # for day_of_week in one_week:
        #     daily_miles = form.daily_miles.data
        #     print("##############################################")
        #     print(daily_miles)
        #     print(day_of_week)            
        #     day = Day(num=day_of_week, mileage_target=daily_miles.day_of_week, miles_completed=0, week=curr_week.id, user=user.id)
            
        #     db.session.add(day)
        #     db.session.commit()
      
        # return redirect('/my-training-plan')


@app.route('/my-training-plan')
def show_plan():
    """Displays plan and allows user to mark off miles as completed"""

    # currently lists everything in display; will fix this later to have dropdowns for each week, or whatever options for displaying more details vs. less

    """ get the current user and current week data from session"""
    user_id = session['user_id']
    user = User.query.get(user_id)
    curr_week = Week.query.get(session['week_id'])

    """ get all the data in this user's plan and display in UI"""
    my_weeks = Week.query.filter(Week.user == user.id).all()
    my_days = Day.query.filter(Day.user == user.id).all()

    return render_template('my_training_plan.html', user=user, curr_week=curr_week.num, my_weeks=my_weeks, my_days=my_days)

@app.route('/weekly-view/<int:week>')
def show_week(week):
    """Displays plan details for single week"""

    """ get current user and week from session and db """
    user_id = session['user_id']
    user = User.query.get(user_id)
    curr_week = Week.query.filter(Week.num == week, Week.user == user_id).first()
    
    """ get user data for days in this week and display in UI"""
    session['week_details'] = curr_week.num
    my_days = Day.query.filter(Day.week == curr_week.num, Day.user == user.id).all()

    return render_template('weekly_details.html', user=user, curr_week=curr_week, my_days=my_days)

@app.route('/weekly-view/<int:week>/edit', methods=["GET", "POST"])
def edit_week(week):
    """Allows user to edit their daily mileage goals"""

    user_id = session['user_id']
    user = User.query.get(user_id)
    # week = Week.query.get(session['week'])
    curr_week = Week.query.filter(Week.num == week).first()
    my_days = Day.query.filter(Day.week == curr_week.num, Day.user == user.id).all()

    ########################################################
    ## this needs to be a WTForm
    ########################################################

    one_week = list(range(1,8))
    if request.method == "POST":
        daily_miles = request.form.to_dict()
        for (day, daily_miles) in daily_miles.items():
            day = Day(num=day, mileage_target=daily_miles, week=week, user=user.id)
            db.session.commit()
        return redirect('/my-training-plan')

    return render_template('daily_miles_form.html', one_week=one_week, week=week)