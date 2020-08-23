import sqlite3
import csv

# TODO::Create database
conn = sqlite3.connect('space.sqlite')
cur = conn.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS Companies
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT UNIQUE,
count INTEGER);

CREATE TABLE IF NOT EXISTS Locations
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
location TEXT UNIQUE);

CREATE TABLE IF NOT EXISTS RocketStatus
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
status TEXT UNIQUE);

CREATE TABLE IF NOT EXISTS MissionStatus
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
status TEXT UNIQUE,
count INTEGER);

CREATE TABLE IF NOT EXISTS Missions
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
company_id INTEGER REFERENCES Companies(id) ON UPDATE CASCADE,
location_id INTEGER REFERENCES Locations(id) ON UPDATE CASCADE,
rocketstatus_id INTERGER REFERENCES RocketStatus(id) ON UPDATE CASCADE,
missionstatus_id INTEGER REFERENCES MissionStatus(id) ON UPDATE CASCADE,
datum TEXT,
detail TEXT,
cost REAL,
year INTEGER,
country_id INTEGER
);
''')


# Read csv file
csvFile = input('Enter CSV file: ')
if len(csvFile) < 1: csvFile = 'Space_Corrected.csv'
commit = 0
with open(csvFile) as spaceCsv:
    spaceReader = csv.reader(spaceCsv, delimiter = ',')
    line = 0
    for row in spaceReader:
        # if line == 11: break
        # print(row)

        # Skip metadata
        if line == 0: 
            line += 1
            continue

        # Read data
        company = row[2]
        location = row[3]
        datum = row[4]
        detail = row[5]
        rocketStatus = row[6][6:]
        try:
            cost = float(row[7].strip())
        except:
            cost = None
        missionStatus = row[8]
        # print(company, location, datum, detail, rocketStatus, cost, missionStatus)

        # TODO::Insert data
        cur.execute('SELECT count FROM Companies WHERE name = ?', (company, ))
        check = cur.fetchone()
        if check is not None:
            cur.execute('UPDATE Companies SET count = count + 1 WHERE name = ?', (company, ))
        else:
            cur.execute('INSERT OR IGNORE INTO Companies (name, count) VALUES (?, 1)', (company, ))
        cur.execute('INSERT OR IGNORE INTO Locations (location) VALUES (?)', (location, ))
        cur.execute('INSERT OR IGNORE INTO RocketStatus (status) VALUES (?)', (rocketStatus, ))
        cur.execute('SELECT count FROM MissionStatus WHERE status = ?', (missionStatus, ))
        check = cur.fetchone()
        if check is not None:
            cur.execute('UPDATE MissionStatus SET count = count + 1 WHERE status = ?', (missionStatus, ))
        else:
            cur.execute('INSERT OR IGNORE INTO MissionStatus (status, count) VALUES (?, 1)', (missionStatus, ))

        cur.execute('SELECT id FROM Companies WHERE name = ?', (company, ))
        company_id = cur.fetchone()[0]
        cur.execute('SELECT id FROM Locations WHERE location = ?', (location, ))
        location_id = cur.fetchone()[0]
        cur.execute('SELECT id FROM RocketStatus WHERE status = ?', (rocketStatus, ))
        rocketstatus_id = cur.fetchone()[0]
        cur.execute('SELECT id FROM MissionStatus WHERE status = ?', (missionStatus, ))
        missionstatus_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Missions (company_id, location_id, rocketstatus_id, missionstatus_id, datum, detail, cost)
         VALUES (?,?,?,?,?,?,?)''', (company_id, location_id, rocketstatus_id, missionstatus_id, datum, detail, cost))

        line += 1
        commit += 1
        if commit % 10 == 0:
            conn.commit()

conn.commit()

print('Number of data:', line - 1)