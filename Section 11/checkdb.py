import sqlite3

conn = sqlite3.connect('./Section 11/contacts.sqlite')

for row in conn.execute('SELECT * FROM contacts'):
    print(row)

conn.close()