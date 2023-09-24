import sqlite3

b = sqlite3.connect('game.db')
a = b.cursor()
a.execute('''CREATE TABLE IF NOT EXISTS users(
name TEXT,
age INTEGER,
password TEXT, INTEGER
)''')
a.execute('''INSERT INTO users VALUES ('Mira', 15, '13579Mira')''')
a.execute('''INSERT INTO users VALUES ('Gera', 90, 'grea567' )''')
a.execute('''INSERT INTO users VALUES ('Brain', 11, '0987654g')''')

b.commit()
b.close()
