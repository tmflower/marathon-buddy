

DROP TABLE users
DROP TABLE weeks
DROP TABLE days

CREATE TABLE users
CREATE TABLE weeks
CREATE TABLE days

INSERT INTO users (
    username,
    password,
    total_miles_completed
)
VALUES 
    ('Sadie',
    'meow',
    10),
    ('Tiny',
    'meow',
    0),
    ('Princess',
    'meow',
    13.8);


INSERT INTO weeks (
    num,
    mileage_target
)
VALUES
    (1, 19),
    (2, 21),
    (3, 25),
    (4, 23);

INSERT INTO days (
    num,
    mileage_target
)
VALUES
    (1, 3),
    (2, 0),
    (3, 4),
    (4, 0),
    (5, 4),
    (6, 0),
    (7, 8)