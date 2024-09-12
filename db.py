import sqlite3

connection = sqlite3.connect('local_db.sqlite3')
cursor = connection.cursor()

#create timer table
cursor.execute("""CREATE TABLE  timers(
    timer_id INT NOT NULL AUTO INCREMENT,
	exercise_mins INT,
	exercise_secs INT,
	rest_mins INT,
	rest_secs INT,
    reps INT,
	PRIMARY KEY (timer_id)
);""")

connection.commit()
connection.close()