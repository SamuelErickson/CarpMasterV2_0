import pandas as pd
import numpy as np

lights = ["Light1"] #List of lights just switched

df_config = pd.read_csv("tankSettings.csv")
df_status = pd.read_csv("tankStatus.csv",index_col=0)


tanks = df_config[df_config['Lights'] == str(lights)]['TankName'].to_list()
n = len(tanks)
if (df_status.loc["LightStatus", tanks].values.all() == 'ON'):
    df_status.loc["LightStatus", tanks] = 'OFF'
elif(df_status.loc["LightStatus", tanks].values.all() == 'OFF'):
    df_status.loc["LightStatus", tanks] = 'ON'
elif (df_status.loc["LightStatus", tanks].values.all() == 'NotConfigured'):
    pass
else:
    df_status.loc["LightStatus", tanks] = 'Error'




df_status.to_csv("tankStatus.csv")
