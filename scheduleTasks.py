#This script edits the RPi cron file
#It clears any currently running cron tasks
#and schedules regular automated tasks

import pandas as pd
from crontab import CronTab
import pandas as pd

#The following line only works in Linux
#https://stackabuse.com/scheduling-jobs-with-python-crontab/
cron = CronTab(user=True)
#remove all existing cron jobs
cron.remove_all()

#Schedule temperature checks
Command1= 'sudo python3 /home/pi/CarpMasterV2_0/example1.py'

job1 = cron.new(command=Command1)
job1.minute.every(1)


#Schedule light on/off switch
Command2 = "python3 /home/pi/CarpMasterV2_0/toggleLight.py"
# Need to add updater here!


job2 = cron.new(command=Command2)
job2.minute.every(1)



# Make web interface reboot upon restart and run as background task
#Command2 = '{ export FLASK_APP=/home/pi/CarpMasterV2_0/app.py; flask run --host=0.0.0.0 & }'

#Command4= 'export FLASK_APP=/home/pi/CarpMasterV2_0/app.py'
#Command3 = 'flask run --host=0.0.0.0 &'








#job2.every_reboot()
#job3 = cron.new(command=Command3)
#job3.every_reboot()

cron.write()

#job.every_reboot()
