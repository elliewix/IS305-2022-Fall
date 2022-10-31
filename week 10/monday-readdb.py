import sqlite3

con = sqlite3.connect('pokedb.db')

cur = con.cursor()

# dump everything out
# cur.execute('SELECT * '
#             'FROM pokemon;')
# results = cur.fetchall()
# # print(results)
# for row in results:
#     print(row)

# run sql queries via pytho

cur.execute('SELECT dex || "-" || name || ".txt", dex, name, description '
            'FROM pokemon '
            'WHERE (name != "") AND (dex != "???");')
results = cur.fetchall()
print(results)

import pathlib

target = pathlib.Path('data')

for r in results:
    p = pathlib.Path(r[0])
    out = target / p
    out.write_text(r[-1])
