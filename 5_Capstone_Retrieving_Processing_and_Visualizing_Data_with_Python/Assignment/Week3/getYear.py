import sqlite3

conn = sqlite3.connect('space.sqlite')
cur = conn.cursor()

# Create Year table
cur.execute('''
CREATE TABLE IF NOT EXISTS Years
(year INTEGER PRIMARY KEY UNIQUE,
count INTEGER)
''')

cur.execute('SELECT id, datum FROM Missions ORDER BY id')
rows = cur.fetchall()

# Update year information
commit = 0
for row in rows:
    id = row[0]
    datum = row[1]
    year = int(datum.split()[3])
    # print(id, year)
    cur.execute('UPDATE Missions SET year = ? WHERE id = ?', (year, id))
    cur.execute('SELECT count FROM Years WHERE year = ?', (year, ))
    check = cur.fetchone()
    if check is not None:
        cur.execute('UPDATE Years SET count = count + 1 WHERE year = ?', (year, ))
    else:
        cur.execute('INSERT OR IGNORE INTO Years (year, count) VALUES (?, 1)', (year, ))

    commit += 1
    if commit % 10 == 0:
        conn.commit()

conn.commit()