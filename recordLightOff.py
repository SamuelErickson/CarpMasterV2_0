import pandas as pd
import numpy as np
import recordActivity as r






    #with open("activityLog.txt", 'a') as csvfile:  # 'a' means append
     #   timeNow = time.asctime()
      #  filewriter = csv.writer(csvfile, delimiter=',') #fix this
       # note = timeNow+","+note
        #filewriter.writerow(note)

lights = ["Light1"] #List of lights just switched
#only one light in current setup, modify if needed

df_config = pd.read_csv("tankSettings.csv")
df_status = pd.read_csv("tankStatus.csv",index_col=0)


tanks = df_config[df_config['Lights'] == str(lights)]['TankName'].to_list()
df_status.loc["LightStatus", tanks] = 'OFF'
df_status.to_csv("tankStatus.csv")




r.recordActivity(__file__)

