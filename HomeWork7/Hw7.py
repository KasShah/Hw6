import sqlite3 as sq

with sq.connect('students.bd') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS student(
    hobby INTEGER,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    year of birth TEXT NOT NULL,
    points fot hw
    )''')

    # cur.execute('''INSERT INTO student VALUES ('write articles', 'Luna', 'Lovegood', 2001, 7)''')
    # cur.execute('''INSERT INTO student VALUES ('Herbology', 'Nevalle', 'Longbottom', 1980, 10)''')
    # cur.execute('''INSERT INTO student VALUES ('Quidditch', 'Dean', 'Thomas', 1980, 5)''')
    # cur.execute('''INSERT INTO student VALUES ('Potions making', 'Severus', 'Snape', 1960, 10)''')
    # cur.execute('''INSERT INTO student VALUES ('Horseback Riding', 'Draco', 'Malfoy', 1980, 9)''')
    # cur.execute('''INSERT INTO student VALUES ('Auror', 'Alastor', 'Moody', 1949, 8)''')
    # cur.execute('''INSERT INTO student VALUES ('Transfiguration', 'Minerva', 'McGonagall', 1935, 10)''')
    # cur.execute('''INSERT INTO student VALUES ('Prohibited items', 'Gellert', 'Grindelwald', 1883, 7)''')
    # cur.execute('''INSERT INTO student VALUES ('serving as an idiote', 'Bellatrix', 'LestrangeBlack', 1951, 5)''')
    # cur.execute('''INSERT INTO student VALUES ('Zoology', 'Newton', 'Sallamander', 1897, 10)''')

    con.commit()

    cur.execute('''UPDATE student SET name = "genius" WHERE points > 10;''')
    cur.execute('''DELETE FROM student WHERE rowid % 2 = 0;''')
    cur.execute('''SELECT * FROM student WHERE surname > 10 ORDER BY surname ASC;''')
    cur.execute('''SELECT * FROM student WHERE name = "genius"''')
    item = cur.fetchall()
    for i in item:
        print(i)

