'''This entire script is commented out because this was only used to create and set up the
tables. The sample data from the csv files in the data_for_db directory was then loaded
into the tables in the ACME database'''

'''import sqlite3

conn = sqlite3.connect('ACME.db')
c = conn.cursor()
c.execute("""CREATE TABLE movies (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name VARCHAR,
          year INTEGER)""")
conn.commit()

c.execute("""CREATE TABLE users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name VARCHAR,
          year_joined INTEGER,
          country VARCHAR)""")
conn.commit()

c.execute("""CREATE TABLE engagement (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          movie_id INTEGER,
          user_id INTEGER,
          watchtime INTEGER)""")

conn.commit()
conn.close()'''