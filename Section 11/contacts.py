import sqlite3

db = sqlite3.connect('./Section 11/contacts.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS contacts(name text, email text)')
db.execute("INSERT INTO contacts VALUES('MUNNA','munna@gmail.com')")
db.execute("INSERT INTO contacts VALUES('monir','monir@gmail.com')")
cursor = db.cursor()
cursor.execute('SELECT * FROM contacts')
for row in cursor:
    print (row)

cursor.close()
db.commit()
db.close()