from flask import *
from toolbox import CountdownBlock
import sqlite3

HIITTrackerAPI = Blueprint('HIITTrackerAPI', __name__)

@HIITTrackerAPI.route("/")
def Index():
    return render_template("home.html")

@HIITTrackerAPI.route("/timer/<string:exerciseminutes>/<string:exerciseseconds>/<string:restminutes>/<string:restseconds>/<string:reps>",
    methods = ["POST"])
def timer(exerciseminutes, exerciseseconds, restminutes, restseconds, reps):
    exerciseTimer = [exerciseminutes, exerciseseconds]
    restTimer = [restminutes, restseconds]
    for rep in reps:
        CountdownBlock(exerciseTimer, restTimer)

@HIITTrackerAPI.route("/newtimer/<string:exerciseminutes>/<string:exerciseseconds>/<string:restminutes>/<string:restseconds>/<string:reps>",
    methods = ["POST"])
def NewTimer(exerciseminutes, exerciseseconds, restminutes, restseconds, reps):
    connection = sqlite3.connect('local_db.sqlite3')
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO timers(
        timer_id INT NOT NULL,
        exercise_mins INT,
        exercise_secs INT,
        rest_mins INT,
        rest_secs INT,
        reps INT,
        PRIMARY KEY (timer_id)
        );""")

    connection.commit()
    connection.close()