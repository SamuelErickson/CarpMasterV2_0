import pandas as pd
import numpy as np
import time

# Write a csv file containing tank names, sensors, etc

#Edit below dictionary with values to reflect configuration of your equipment
TankConfig = {'TankName': ["Tank_A1", "Tank_A2","Tank_B1", "Tank_B2","Tank_D1", "Tank_D2"],
                'Status':["Online", "Online","Under Construction", "Under Construction","Online", "Online"],
                'TempSensor': ["Thermo1", "Thermo2","None","None","None","None"],
                #Edit line below with serial numbers of your DS18B20 temp sensors!
                'TempSensorSerialID':["ID#", "ID#","None","None","None","None"],
                'TempSetPoint': ["16", "16","NA","NA","Variable","Variable"],
                'Lights': [["Light1"], ["Light1"],"Other","Other","Other","Other"],
                "Photoperiod (h)":[12,12,"NA","NA",16,16],
                'LightsOnTime': ["5:00","5:00","5:00","5:00","5:00","5:00"],
                'LightsOffTime': ["21:00","21:00","21:00","21:00","21:00","21:00"]

                }
LightSettings = {'LightName': ["Light1"],'TimeOn': ["5:00"],'TimeOff':["21:00"],"Photoperiod":[str(16)+" Hours"]}

#Function: Initialize lights!
timeNow = time.asctime()
#CHECK whether light should be on right now or off right now and set up lights...




df_TankStatus = pd.DataFrame(columns=TankConfig["TankName"],index=["Temp","LightStatus"])


#Start some tanks right away, need to check time first
#tanks = ['Tank_A1', 'Tank_A2']
#df_TankStatus.loc["LightStatus", tanks] = 'ON'


df_TankConfig = pd.DataFrame(data=TankConfig)
df_LightSettings = pd.DataFrame(data=LightSettings)

df_Thermo1 = pd.DataFrame(columns=["Time","Temp"])

df_TempData = pd.DataFrame(columns=["Time","Sensor","Temp"])

df_TankConfig.to_csv("tankSettings.csv",index=False)
df_LightSettings.to_csv("lightSettings.csv",index=False)
df_Thermo1.to_csv("thermo1.csv",index=False)

df_TempData.to_csv("tempData.csv",index=False)

df_TankStatus.to_csv("tankStatus.csv")



print(df_LightSettings)
print(df_TankConfig)
print(df_Thermo1)
print(df_TankStatus)


# Write a csv file containing tank temps short term
# Write a csv file containing tank temps long term


# def initialize():
#     global numRows
#     global relaySts
#     numRows = 0
#     temp, hum = (16,30)
#     # Add whether light should start out on or off...
#
#
#     #colString = "Time,Humidity,Temperature"
#     colString = "Time,Humidity,Temperature,HumidifierPower"
#     with open('HumTempData_ShortTerm.csv', 'w') as s:
#         s.write(colString)
#     if not os.path.isfile('HumTempData_LongTerm.csv'):
#         with open('HumTempData_LongTerm.csv', 'w') as s:
#             s.write(colString)