import numpy as np
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('space.sqlite')
cur = conn.cursor()

# Retrieve from tuple
def clean(rows, data):
    for row in rows:
        data.append(row[0])

# Read year info
def readYear():
    years = []
    yrcounts = []

    cur.execute('SELECT year FROM Years ORDER BY year')
    rows = cur.fetchall()
    clean(rows, years)
    cur.execute('SELECT count FROM Years ORDER BY year')
    rows = cur.fetchall()
    clean(rows, yrcounts)

    return years, yrcounts

# Read company info
def readCompany():
    companies = []
    comcounts = []

    cur.execute('SELECT name FROM Companies ORDER BY count DESC LIMIT 10')
    rows = cur.fetchall()
    clean(rows, companies)
    cur.execute('SELECT count FROM Companies ORDER BY count DESC LIMIT 10')
    rows = cur.fetchall()
    clean(rows, comcounts)

    return companies, comcounts

# Read country info
def readCountry():
    countries = []
    councounts = []

    cur.execute('SELECT name FROM Countries ORDER BY count DESC LIMIT 10')
    rows = cur.fetchall()
    clean(rows, countries)
    cur.execute('SELECT count FROM Countries ORDER BY count DESC LIMIT 10')
    rows = cur.fetchall()
    clean(rows, councounts)

    return countries, councounts

# Plot
def plot(x, y, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

# Bar
def bar(x, y, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


# Call read function
years, yrcounts = readYear()
companies, comcounts = readCompany()
countries, councounts = readCountry()

# Call plot functions
plot(years, yrcounts, 'Number of Space Missions per Year', 'Year', 'Number of Missions')
bar(companies, comcounts, 'Number of Space Missions per Company', 'Company', 'Number of Space Missions')
bar(countries, councounts, 'Number of Space Missions per Country', 'Country', 'Number of Space Missions')


plt.show()

