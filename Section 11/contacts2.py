import sqlite3
db = sqlite3.connect('./Section 11/contacts.sqlite')
update_sql = 'UPDATE contacts SET email="mahadi@gmail.com" WHERE name="MUNNA"'
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print(f'{update_cursor.rowcount} rows are updated')
update_cursor.connection.commit()
print(f'update_cursor.connection is same as db: {update_cursor.connection == db}')
for name, email in db.execute('SELECT * FROM contacts'):
    print (name)
    print (email)
    print('-'*20)

db.close()