#This script edits the RPi cron file
#to schedule regular automated tasks

from crontab import CronTab


#There are five ways to include a job in cron
#The following line only works in Linux
#https://stackabuse.com/scheduling-jobs-with-python-crontab/
cron = CronTab(user=True)
cron.remove_all()  #remove all existing cron jobs
Command1= '/home/pi/CarpMasterV2_0/python example1.py'

job1 = cron.new(command=Command1)
job1.minute.every(1)
cron.write()

#job.every_reboot()
