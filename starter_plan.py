from models import db, Week, Day, User
from flask import session


def setup_starter_plan():

    user_id = session['user_id']
    user = User.query.get(user_id)
    user.num_weeks = 16;

    week1 = Week(num = 1, mileage_target = 19, user = user.id)
    week2 = Week(num = 2, mileage_target = 21, user = user.id)
    week3 = Week(num = 3, mileage_target = 25, user = user.id)
    week4 = Week(num = 4, mileage_target = 23, user = user.id)
    week5 = Week(num = 5, mileage_target = 30, user = user.id)
    week6 = Week(num = 6, mileage_target = 32, user = user.id)
    week7 = Week(num = 7, mileage_target = 28, user = user.id)
    week8 = Week(num = 8, mileage_target = 35, user = user.id)
    week9 = Week(num = 9, mileage_target = 39, user = user.id)
    week10 = Week(num = 10, mileage_target = 35, user = user.id)
    week11 = Week(num = 11, mileage_target = 41, user = user.id)
    week12 = Week(num = 12, mileage_target = 31, user = user.id)
    week13 = Week(num = 13, mileage_target = 42, user = user.id)
    week14 = Week(num = 14, mileage_target = 30, user = user.id)
    week15 = Week(num = 15, mileage_target = 23, user = user.id)
    week16 = Week(num = 16, mileage_target = 34, user = user.id)
    weeks = (week1, week2, week3, week4, week5, week6, week7, week8, week9, week10, week11, week12, week13, week14, week15, week16)
    for week in weeks:
        db.session.add(week)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week1.id, user=user.id)
    day2 = Day(num=2, mileage_target=3, week=week1.id, user=user.id)
    day3 = Day(num=3, mileage_target=4, week=week1.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week1.id, user=user.id)
    day5 = Day(num=5, mileage_target=4, week=week1.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week1.id, user=user.id)
    day7 = Day(num=7, mileage_target=8, week=week1.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week2.id, user=user.id)
    day2 = Day(num=2, mileage_target=3, week=week2.id, user=user.id)
    day3 = Day(num=3, mileage_target=4, week=week2.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week2.id, user=user.id)
    day5 = Day(num=5, mileage_target=4, week=week2.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week2.id, user=user.id)
    day7 = Day(num=7, mileage_target=10, week=week2.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week3.id, user=user.id)
    day2 = Day(num=2, mileage_target=4, week=week3.id, user=user.id)
    day3 = Day(num=3, mileage_target=5, week=week3.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week3.id, user=user.id)
    day5 = Day(num=5, mileage_target=5, week=week3.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week3.id, user=user.id)
    day7 = Day(num=7, mileage_target=11, week=week3.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week4.id, user=user.id)
    day2 = Day(num=2, mileage_target=4, week=week4.id, user=user.id)
    day3 = Day(num=3, mileage_target=5, week=week4.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week4.id, user=user.id)
    day5 = Day(num=5, mileage_target=5, week=week4.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week4.id, user=user.id)
    day7 = Day(num=7, mileage_target=9, week=week4.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week5.id, user=user.id)
    day2 = Day(num=2, mileage_target=5, week=week5.id, user=user.id)
    day3 = Day(num=3, mileage_target=6, week=week5.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week5.id, user=user.id)
    day5 = Day(num=5, mileage_target=6, week=week5.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week5.id, user=user.id)
    day7 = Day(num=7, mileage_target=13, week=week5.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week6.id, user=user.id)
    day2 = Day(num=2, mileage_target=5, week=week6.id, user=user.id)
    day3 = Day(num=3, mileage_target=6, week=week6.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week6.id, user=user.id)
    day5 = Day(num=5, mileage_target=6, week=week6.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week6.id, user=user.id)
    day7 = Day(num=7, mileage_target=15, week=week6.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week7.id, user=user.id)
    day2 = Day(num=2, mileage_target=5, week=week7.id, user=user.id)
    day3 = Day(num=3, mileage_target=7, week=week7.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week7.id, user=user.id)
    day5 = Day(num=5, mileage_target=6, week=week7.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week7.id, user=user.id)
    day7 = Day(num=7, mileage_target=10, week=week7.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week8.id, user=user.id)
    day2 = Day(num=2, mileage_target=5, week=week8.id, user=user.id)
    day3 = Day(num=3, mileage_target=7, week=week8.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week8.id, user=user.id)
    day5 = Day(num=5, mileage_target=7, week=week8.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week8.id, user=user.id)
    day7 = Day(num=7, mileage_target=16, week=week8.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week9.id, user=user.id)
    day2 = Day(num=2, mileage_target=6, week=week9.id, user=user.id)
    day3 = Day(num=3, mileage_target=8, week=week9.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week9.id, user=user.id)
    day5 = Day(num=5, mileage_target=7, week=week9.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week9.id, user=user.id)
    day7 = Day(num=7, mileage_target=18, week=week9.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week10.id, user=user.id)
    day2 = Day(num=2, mileage_target=6, week=week10.id, user=user.id)
    day3 = Day(num=3, mileage_target=8, week=week10.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week10.id, user=user.id)
    day5 = Day(num=5, mileage_target=7, week=week10.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week10.id, user=user.id)
    day7 = Day(num=7, mileage_target=14, week=week10.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week11.id, user=user.id)
    day2 = Day(num=2, mileage_target=6, week=week11.id, user=user.id)
    day3 = Day(num=3, mileage_target=8, week=week11.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week11.id, user=user.id)
    day5 = Day(num=5, mileage_target=8, week=week11.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week11.id, user=user.id)
    day7 = Day(num=7, mileage_target=19, week=week11.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week12.id, user=user.id)
    day2 = Day(num=2, mileage_target=6, week=week12.id, user=user.id)
    day3 = Day(num=3, mileage_target=6, week=week12.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week12.id, user=user.id)
    day5 = Day(num=5, mileage_target=6, week=week12.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week12.id, user=user.id)
    day7 = Day(num=7, mileage_target=13, week=week12.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week13.id, user=user.id)
    day2 = Day(num=2, mileage_target=6, week=week13.id, user=user.id)
    day3 = Day(num=3, mileage_target=8, week=week13.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week13.id, user=user.id)
    day5 = Day(num=5, mileage_target=8, week=week13.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week13.id, user=user.id)
    day7 = Day(num=7, mileage_target=20, week=week13.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week14.id, user=user.id)
    day2 = Day(num=2, mileage_target=6, week=week14.id, user=user.id)
    day3 = Day(num=3, mileage_target=6, week=week14.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week14.id, user=user.id)
    day5 = Day(num=5, mileage_target=6, week=week14.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week14.id, user=user.id)
    day7 = Day(num=7, mileage_target=12, week=week14.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week15.id, user=user.id)
    day2 = Day(num=2, mileage_target=6, week=week15.id, user=user.id)
    day3 = Day(num=3, mileage_target=5, week=week15.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week15.id, user=user.id)
    day5 = Day(num=5, mileage_target=4, week=week15.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week15.id, user=user.id)
    day7 = Day(num=7, mileage_target=8, week=week15.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()

    day1 = Day(num=1, mileage_target=0, week=week16.id, user=user.id)
    day2 = Day(num=2, mileage_target=3, week=week16.id, user=user.id)
    day3 = Day(num=3, mileage_target=3, week=week16.id, user=user.id)
    day4 = Day(num=4, mileage_target=0, week=week16.id, user=user.id)
    day5 = Day(num=5, mileage_target=2, week=week16.id, user=user.id)
    day6 = Day(num=6, mileage_target=0, week=week16.id, user=user.id)
    day7 = Day(num=7, mileage_target=26.2, week=week16.id, user=user.id)
    days = (day1, day2, day3, day4, day5, day6, day7)
    for day in days:
        db.session.add(day)
        db.session.commit()