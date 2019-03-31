import pandas as pd
import numpy as np

# Write a csv file containing tank names, sensors, etc


TankSettings = {'TankName': ["Tank_A1", "Tank_A2"], 'Thermo': ["Thermo1", "Thermo2"],'TempSetPoint': ["16", "16"],
            'Light': ["Light1", "Light1"]}
LightSettings = {'LightName': ["Light1"],'TimeOn': ["5:00"],'TimeOff':["21:00"],"Photoperiod":[str(16)+" Hours"]}
df_TankSettings = pd.DataFrame(data=TankSettings,columns=["TankName","Light","Thermo","TempSetPoint"])
df_LightSettings = pd.DataFrame(data=LightSettings)

print(df_LightSettings)
print(df_TankSettings)
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