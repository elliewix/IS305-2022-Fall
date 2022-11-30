import sqlite3, time, os

# Delete the database if it already exists:
if os.path.exists('deleteme.db'):
	os.unlink('deleteme.db')

# Create the database table
conn = sqlite3.connect('demo.db', isolation_level=None)
cur = conn.cursor()
conn.execute('create table if not exists demo (a int, b int, c int)')

# Time how long it takes to insert 4000 records:
st = time.time()
for i in range(4000):
	conn.execute('insert into demo values (1,1,1)')
print(round(time.time() - st, 1))

# Time how long it takes to read 4000 records 4000 times:
st = time.time()
for i in range(4000):
	x= conn.execute('select * from demo').fetchall()
print(round(time.time() - st, 1))

conn.close()

# Delete the test database:
if os.path.exists('deleteme.db'):
	os.unlink('deleteme.db')

conn = sqlite3.connect('demo.db', isolation_level='DEFERRED')
cur = conn.cursor()
conn.execute('create table if not exists demo (a int, b int, c int)')

# Time how long it takes to insert 4000 records:
st = time.time()
for i in range(4000):
	conn.execute('insert into demo values (1,1,1)')
print(round(time.time() - st, 1))

conn.commit()

# Time how long it takes to read 4000 records 4000 times:
st = time.time()
for i in range(4000):
	x= conn.execute('select * from demo').fetchall()
print(round(time.time() - st, 1))

# Delete the test database:
if os.path.exists('deleteme.db'):
	os.unlink('deleteme.db')
