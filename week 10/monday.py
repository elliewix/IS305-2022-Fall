import sqlite3
import csv

with open('pokemon_names_and_descriptions.csv', 'r', encoding='utf-8') as infile:
    csvin = csv.reader(infile)
    headers = next(csvin)
    data = [r for r in csvin]

# print(headers, len(data))

# create connection

con = sqlite3.connect('pokedb.db')

cur = con.cursor()
print(headers)
cur.execute('CREATE TABLE pokemon (dex text, name text, description text);')

cur.executemany('INSERT INTO pokemon VALUES (?, ?, ?)', data)

con.commit()

