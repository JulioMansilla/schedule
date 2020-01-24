from datetime import datetime

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
day = int(datetime.now().weekday()) #0-6
dayOfTheWeek = week[day]
hour = datetime.now().hour
mins = datetime.now().minute


def inMin(hour, min):
    return (hour*60) + min

def time():
    timeInmins = (hour*60)+mins

    if timeInmins<=inMin(8, 30):
        period = 0
    elif timeInmins<=inMin(9, 15):
        period = 1
    elif timeInmins<=inMin(10, 0):
        period = 2
    elif timeInmins<=inMin(10, 45):
        period = 3
    elif timeInmins<=inMin(10, 55):
        period = 4
    elif timeInmins<=inMin(11, 40):
        period = 5
    elif timeInmins<=inMin(12, 25):
        period = 6
    elif timeInmins<=inMin(13, 10):
        period = 7
    elif timeInmins<=inMin(13, 55):
        period = 8
    elif timeInmins<=inMin(14, 40):
        period = 9
    else:
        period = 10

    time = {
        "hour": hour,
        "mins": mins,
        "day": dayOfTheWeek,
        "dayNum": day,
        "period": period,
        "timeInMins": timeInmins
    }

    return time
