import pandas as pd
import random
import time
import SendEmailAlert as sea

def getTemp(id):
    # Pass ID number of thermometer, get value
    return 16 + random.random()*5
# Step one, get thermometers to check

df_config = pd.read_csv("tankSettings.csv")
df_config = df_config[df_config['TempSensor']!="None"]
df_config = df_config[['TankName','TempSensor','TempSensorSerialID','TempSetPoint']]
# df2 = pd.read_csv("thermo2.csv")

df1 = pd.read_csv("thermo1.csv")

df_tempData = pd.read_csv("tempData.csv")
df_status = pd.read_csv("tankStatus.csv",index_col=0)

for sensor in df_config["TempSensor"].tolist():
    # Iterate over all temp sensors, measure and save values
    timeNow = time.asctime()
    T = getTemp("blank")
    df_tempData = df_tempData.append({"Time": timeNow, "Sensor":sensor, "Temp": T}, ignore_index=True)
    #df_status[sensor]
    #Following line finds the names of the tanks associated with the current sensor
    # being iterated over, returns array
    tanks = df_config[df_config['TempSensor'] == sensor]['TankName'].to_list()
    df_status.loc["Temp", tanks] = T

for row in df_config.iterrows():
    print(row)

#Step two, get temperature values





t1 = 16 + random.random()*5
t2 = 16 + random.random()*5

#Step three, update short term data file

timeNow = time.asctime()
#df1 = df1.append({"Time":timeNow,"Temp":t1},ignore_index=True)
#df1.to_csv("thermo1.csv",index=False)

df_tempData.to_csv("tempData.csv",index=False)
df_status.to_csv("tankStatus.csv")


#Step four, Append results to long term data file

if True or t1 > 30:
    sea.sendEmailAlert("Error temp too high")