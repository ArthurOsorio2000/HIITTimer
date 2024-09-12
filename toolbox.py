import time
import datetime

def Countdown(m, s):
    totalSeconds = (m * 60) + s
    while totalSeconds > 0:
        timer = datetime.timedelta(seconds = totalSeconds)
        print(timer, end ='\r')
        #sleep waits one second once passed
        time.sleep(1)
        totalSeconds -= 1
    
    print("timer done")

def CountdownBlock(exerciseTimeArray, restTimeArray):
    Countdown(exerciseTimeArray[0], exerciseTimeArray[1])
    Countdown(restTimeArray[0], restTimeArray[1])