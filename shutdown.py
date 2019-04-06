# This script shuts down CarpMaster. It does not uninstall
# any code, but it prevents any further action

from crontab import CronTab


#clear the crontab file of scheduled tasks:
cron = CronTab(user=True)
cron.remove_all()  #remove


# Need to add code here to turn kill all ongoing processes