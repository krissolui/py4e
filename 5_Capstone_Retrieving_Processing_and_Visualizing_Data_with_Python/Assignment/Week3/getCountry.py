import sqlite3

conn = sqlite3.connect('space.sqlite')
cur = conn.cursor()

# Create Country table
cur.execute('''
CREATE TABLE IF NOT EXISTS Countries
(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT,
count INTEGER)
''')


cur.execute('SELECT id, location_id FROM Missions ORDER BY id')
rows = cur.fetchall()

# Update country information
commit = 0
for row in rows:
    id = row[0]
    location_id = row[1]
    cur.execute('SELECT location FROM Locations WHERE id = ?', (location_id, ))
    location = cur.fetchone()[0]
    info = location.split()
    country = info[-1]
    # print(id, country)

    # Update table Countries
    cur.execute('SELECT count FROM Countries WHERE name = ?', (country, ))
    check = cur.fetchone()
    if check is not None:
        cur.execute('UPDATE Countries SET count = count + 1 WHERE name = ?', (country, ))
    else:
        cur.execute('INSERT INTO Countries (name, count) VALUES (?, 1)', (country, ))

    # Update table Missions column country
    cur.execute('SELECT id FROM Countries WHERE name = ?', (country, ))
    country_id = cur.fetchone()[0]
    cur.execute('UPDATE Missions SET country_id = ? WHERE id = ?', (country_id, id))

    commit += 1
    if commit % 10 == 0:
        conn.commit()

conn.commit()