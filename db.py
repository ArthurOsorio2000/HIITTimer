import sqlite3

connection = sqlite3.connect('local_db.sqlite3')

cursor = connection.cursor()

connection.commit()
connection.close()