import sqlalchemy
import pprint

db = 'postgresql://postgres:zxcvbn123@localhost:5432/netology1102'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

ss = connection.execute("""
SELECT title,releaseyear from albums
WHERE releaseyear = 2018;
                            """).fetchall()

print('\nНазвание и год выхода альбомов, вышедших в 2018 году;')
pprint.pprint(ss)

ss = connection.execute("""
SELECT title, duration from tracks
ORDER BY duration DESC
LIMIT 1;
                            """).fetchall()

print('\nНазвание и продолжительность самого длительного трека;')
pprint.pprint(ss)

ss = connection.execute("""
SELECT title from tracks
WHERE duration >= '00:03:30'
                            """).fetchall()

print('\nНазвание треков, продолжительность которых не менее 3,5 минуты;')
pprint.pprint(ss)

ss = connection.execute("""
SELECT title from collections
WHERE releaseyear BETWEEN 2018 and 2020;
                            """).fetchall()

print('\nНазвания сборников, вышедших в период с 2018 по 2020 год включительно;')
pprint.pprint(ss)

ss = connection.execute("""
SELECT name from performers
WHERE name NOT LIKE '%% %%'
                            """).fetchall()

print('\nИсполнители, чье имя состоит из 1 слова;')
pprint.pprint(ss)

ss = connection.execute("""
SELECT * from tracks
WHERE title LIKE '%%my%%'
                            """).fetchall()

print('\nНазвание треков, которые содержат слово "мой"/"my".')
pprint.pprint(ss)
