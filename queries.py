import sqlite3

conn = sqlite3.connect('ACME.db')
c = conn.cursor()

'''Top 3 countries in terms of numbers of users'''
c.execute("""SELECT country, ranks FROM(
        SELECT country, 
        DENSE_RANK() OVER(ORDER BY COUNT(country) DESC) AS ranks
        FROM users
        GROUP BY country) ranked_countries
    WHERE ranks <= 3""")
print(c.fetchall())

'''Bottom 3 countries in terms of numbers of users'''
c.execute("""SELECT country, ranks FROM(
        SELECT country, 
        DENSE_RANK() OVER(ORDER BY COUNT(country) ASC) AS ranks
        FROM users
        GROUP BY country) ranked_countries
    WHERE ranks <= 3""")
print(c.fetchall())

'''Users who do not have their engagement data collected'''
c.execute("""SELECT first_name, last_name, year_joined FROM users
            WHERE year_joined < 2021""")
print(c.fetchall())

'''Recommendation to users in different countries based on maximum movie watchtime in the country'''
c.execute("""
            WITH watched_movies AS(
                SELECT movies.name, users.country, SUM(engagement.watchtime) AS tot_watchtime,
                DENSE_RANK() OVER(PARTITION BY country ORDER BY SUM(engagement.watchtime) DESC) AS ranks
                FROM engagement
                JOIN users ON users.id = user_id
                JOIN movies ON movies.id = movie_id
                GROUP BY movie_id, country)
            SELECT name, country, ranks 
            FROM watched_movies
            WHERE ranks = 1
""")
print(c.fetchall())

conn.close()