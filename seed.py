from models import db, User, Week, Day
from app import app

db.drop_all()
db.create_all()

User.query.delete()
Week.query.delete()
Day.query.delete()


db.session.add_all([
User(username='Sadie', password='meow', total_miles_completed=10, num_weeks=30),
User(username='Tiny', password='meow', total_miles_completed=3, num_weeks=24),
User(username='Princess', password='meow', total_miles_completed=12.8)
])
db.session.commit()


db.session.add_all([
Week(num=1, mileage_target=19, user=1),
Week(num=2, mileage_target=21, user=1),
Week(num=3, mileage_target=25, user=1),
Week(num=4, mileage_target=23, user=1),
Week(num=1, mileage_target=19, user=2),
Week(num=2, mileage_target=21, user=2),
Week(num=3, mileage_target=25, user=2),
Week(num=4, mileage_target=23, user=2),
Week(num=1, mileage_target=19, user=3),
Week(num=2, mileage_target=21, user=3),
Week(num=3, mileage_target=25, user=3),
Week(num=4, mileage_target=23, user=3)
])
# db.session.add_all([user1, user2, user3, week1, week2, week3, week4])
db.session.commit()


db.session.add_all([
Day(num=1, mileage_target=3, week=1, user=1),
Day(num=2, mileage_target=0, week=1, user=1),
Day(num=3, mileage_target=4, week=1, user=1),
Day(num=4, mileage_target=0, week=1, user=1),
Day(num=5, mileage_target=4, week=1, user=1),
Day(num=6, mileage_target=0, week=1, user=1),
Day(num=7, mileage_target=8, week=1, user=1),
Day(num=1, mileage_target=3, week=2, user=1),
Day(num=2, mileage_target=0, week=2, user=1),
Day(num=3, mileage_target=4, week=2, user=1),
Day(num=4, mileage_target=0, week=2, user=1),
Day(num=5, mileage_target=4, week=2, user=1),
Day(num=6, mileage_target=0, week=2, user=1),
Day(num=7, mileage_target=8, week=2, user=1),
Day(num=1, mileage_target=3, week=3, user=1),
Day(num=2, mileage_target=0, week=3, user=1),
Day(num=3, mileage_target=4, week=3, user=1),
Day(num=4, mileage_target=0, week=3, user=1),
Day(num=5, mileage_target=4, week=3, user=1),
Day(num=6, mileage_target=0, week=3, user=1),
Day(num=7, mileage_target=8, week=3, user=1),
Day(num=1, mileage_target=3, week=4, user=1),
Day(num=2, mileage_target=0, week=4, user=1),
Day(num=3, mileage_target=4, week=4, user=1),
Day(num=4, mileage_target=0, week=4, user=1),
Day(num=5, mileage_target=4, week=4, user=1),
Day(num=6, mileage_target=0, week=4, user=1),
Day(num=7, mileage_target=8, week=4, user=1)
])
# db.session.add_all([day1, day2, day3, day4, day5, day6, day7])
db.session.commit()