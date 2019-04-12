import pandas as pd
import numpy as np
import recordActivity as r


lights = ["Light1"] #List of lights just switched
#only one light in current setup, modify if needed

df_config = pd.read_csv("tankConfig.csv")
df_status = pd.read_csv("tankStatus.csv",index_col=0)


tanks = df_config[df_config['Lights'] == str(lights)]['TankName'].to_list()
df_status.loc["LightStatus", tanks] = 'ON'
df_status.to_csv("tankStatus.csv")



r.recordActivity(__file__)


