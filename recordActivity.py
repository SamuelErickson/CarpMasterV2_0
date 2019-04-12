import time
import os

def recordActivity(fileName):
    # records time, name of script and appends to activity log file
    # ALWAYS call this function with tankConfig.csv as the argument
    # Example: r.recordActivity(__file__)

    note = os.path.basename(fileName)
    timeNow = time.asctime()
    note = timeNow + "," + note+"\n"
    f = open("activityLog.txt", 'a+')
    f.writelines(note)
    f.close()

