import pandas as pd
import random
import time
import os
import glob
import RPi.GPIO as GPIO
import SendEmailAlert as sea

def configureDS18B20():
    #code adapted from Adafruit tutorial
    # https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software
    #global device_file
    global device_files
    # Commands to start interface running
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    # Find file from which temperature data can be read
    base_dir = '/sys/bus/w1/devices/'
    # I need to modify this to be a list rather than a single
    # Folder!
    device_folder = glob.glob(base_dir + '28*')
    device_files = [i + '/w1_slave' for i in device_folder] # A list comprehension
    #device_file = device_folder[0]
    #device_file = device_folder[0] + '/w1_slave'

def read_temp_raw(device_file):
    # Code taken from Adafruit DS18B20 tutorial
    # Reads data from a text file
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    # Code taken from Adafruit DS18B20 tutorial
    # Reads data from the file on the RPi reporting temperature data
    # Checks for errors, extracts results
    # I modified to only return celcius
    temp_list = []
    for file in device_files:
        print("reading from "+file)
        lines = read_temp_raw(file)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            temp_list = temp_list+[temp_c]
    return temp_list


configureDS18B20()
temps = read_temp() # get list of temperatures

df_config = pd.read_csv("tankSettings.csv") # get the tank configuration
df_config = df_config[df_config['TempSensor']!="None"] # Remove tanks which don't have thermos
df_config = df_config[['TankName','TempSensor','TempSensorSerialID','TempSetPoint']] # Variables of interest

df_tempData = pd.read_csv("tempData.csv") # open temp data log file
df_status = pd.read_csv("tankStatus.csv",index_col=0) # open current status file



i = 0
for sensor in df_config["TempSensor"].tolist():
    # Iterate over all temp sensors, measure and save values
    timeNow = time.asctime()
    T = temps[i]
    df_tempData = df_tempData.append({"Time": timeNow, "Sensor":sensor, "Temp": T}, ignore_index=True)
    #df_status[sensor]
    #Following line finds the names of the tanks associated with the current sensor
    # being iterated over, returns array
    tanks = df_config[df_config['TempSensor'] == sensor]['TankName'].values.to_list()
    df_status.loc["Temp", tanks] = T

#df2 = pd.read_csv("thermo2.csv")

#t1 = 16 + random.random()*5
#t1 = read_temp()
#t2 = "No Sensor Configured"
#print(t1)

#t2 = 16 + random.random()*5

#time = time.asctime()
#df1 = df1.append({"Time":time,"Temp":t1},ignore_index=True)
#df1.to_csv("thermo1.csv",index=False)

#df1 = df1.append({"Time":timeNow,"Temp":t1},ignore_index=True)
#df1.to_csv("thermo1.csv",index=False)

df_tempData.to_csv("tempData.csv",index=False)
df_status.to_csv("tankStatus.csv")


#Step four, Append results to long term data file

if True or 25 > 30:
    sea.sendEmailAlert("Error temp too high")



print("temperature logged")

