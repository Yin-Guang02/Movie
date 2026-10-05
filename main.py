import sqlite3
import pandas as pd
conn= sqlite3.connect('database.db')
cursor= conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Movie_Actor;

CREATE TABLE Movie(
movie_id INTEGER PRIMARY KEY,
title TEXT,
genre TEXT,
year INTEGER,
rating REAL,
duration INTEGER
);

CREATE TABLE Actor(

actor_id INTEGER PRIMARY KEY,
actor_name TEXT,
birth_year INTEGER,
country TEXT
);

CREATE TABLE Movie_Actor(
movie_id INTEGER,
actor_id INTEGER
);

INSERT INTO Movie VALUES
(1,'The Lion King','Animation',1994,8.5,88),

(2,'Toy Story','Animation',1995,8.3,81),

(3,'Frozen','Animation',2013,7.4,102),

(4,'Moana','Animation',2016,7.6,107),

(5,'Spider-Man','Action',2002,7.3,121),

(6,'Black Panther','Action',2018,7.3,134),

(7,'Avengers','Action',2012,8.0,143),

(8,'Matilda','Drama',1996,7.0,98),

(9,'Home Alone','Comedy',1990,7.7,103),

(10,'Elf','Comedy',2003,6.9,97),

(11,'Coco','Animation',2017,8.4,105),

(12,'Interstellar','Drama',2014,8.6,169);

INSERT INTO Actor VALUES

(1,'Tom Hanks',1956,'USA'),

(2,'Idris Elba',1972,'UK'),

(3,'Chadwick Boseman',1976,'USA'),

(4,'Scarlett Johansson',1984,'USA'),

(5,'Macaulay Culkin',1980,'USA'),

(6,'Will Smith',1968,'USA'),

(7,'Meryl Streep',1949,'USA'),

(8,'Lupita Nyongo',1983,'Kenya'),

(9,'Priyanka Chopra',1982,'India'),

(10,'Jackie Chan',1954,'China');

INSERT INTO Movie_Actor VALUES

(1,2),(2,1),(5,1),(6,3),(6,8),(7,4),(8,7),(9,5),(11,2),(12,1);

""")

conn.commit()
print('Database ready!')
genres = pd.read_sql("""SELECT DISTINCT(genre)
FROM Movie;""",conn)
print(genres)

countries= pd.read_sql("""SELECT DISTINCT(Country)
FROM actor;""",conn)
print(countries)

top_movies=pd.read_sql("""SELECT Title,Genre,Rating
FROM Movie
ORDER BY Rating DESC;""",conn)
print(top_movies)

oldest_first= pd.read_sql("""SELECT Title,year
FROM Movie
ORDER BY Year;""",conn)
print(oldest_first)

youngest_actors = pd.read_sql("""SELECT actor_name,birth_yeat,country
FROM Actor
ORDER BY birth_year DESC;""",conn)
print(youngest_actors)