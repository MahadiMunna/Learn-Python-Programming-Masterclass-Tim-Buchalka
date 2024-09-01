import sqlite3

db = sqlite3.connect('./Section 11/contacts.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS contacts(name text, email text)')
db.execute("INSERT INTO contacts VALUES('MUNNA','munna@gmail.com')")

cursor = db.cursor()
cursor = db.execute('SELECT * FROM contacts')
for row in cursor:
    print (row)