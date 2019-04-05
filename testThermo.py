import os
import glob
import time
import subprocess

#from https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'

device_file_list = glob.glob(base_dir + '28*')
for folder in device_file_list:
    folder = folder + '/w1_slave'

#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'


def read_temp_raw(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(device_folder_list):
    print("reading temp...")
    print("the device folder list is "+str(device_folder_list))
    output = []
    for file in device_folder_list:
        lines = read_temp_raw(file)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw(file)
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
        print("first temp is"+temp_c)
        output = output+temp_c
    return output

def read_temp_raw(filename):
    catdata = subprocess.Popen(['cat',filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = catdata.communicate()
    out_decode = out.decode('utf-8')
    lines = out_decode.split('\n')
    return lines

while True:
    print(read_temp(device_file_list))
    #deg_c, deg_f = read_temp()
    time.sleep(1)