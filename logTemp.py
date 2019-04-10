import pandas as pd
import random
import time
import os
import glob
import RPi.GPIO as GPIO

def configureDS18B20():
    #code adapted from Adafruit tutorial
    # https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software
    global device_file
    # Commands to start interface running
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    # Find file from which temperature data can be read
    base_dir = '/sys/bus/w1/devices/'
    # I need to modify this to be a list rather than a single
    # Folder!
    device_folder = glob.glob(base_dir + '28*')
    print(device_folder)
    [i + '/w1_slave' for i in device_folder] # A list comprehension
    print(device_folder)
    #device_file = device_folder[0] + '/w1_slave'

def read_temp_raw():
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
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c


def main():
    configureDS18B20()
    print(read_temp_raw())

main()


df1 = pd.read_csv("thermo1.csv")


#df2 = pd.read_csv("thermo2.csv")

#t1 = 16 + random.random()*5
t1 = read_temp()
t2 = "No Sensor Configured"
print(t1)

#t2 = 16 + random.random()*5

time = time.asctime()
#df1 = df1.append({"Time":time,"Temp":t1},ignore_index=True)
#df1.to_csv("thermo1.csv",index=False)
print("temperature logged")