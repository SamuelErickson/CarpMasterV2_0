from datetime import datetime
myFile = open('/home/pi/append.txt', 'a')
myFile.write('\nAccessed on ' + str(datetime.now()))