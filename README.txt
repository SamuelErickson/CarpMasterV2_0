To set up this package on a Raspberry pi, run the following lines:

#First, set up a virtual environment for code to execute in
sudo pip3 install virtualenv
virtualenv -p python3 myenv

# Download all needed code from github
git clone https://github.com/SamuelErickson/CarpMasterV2_0.git
sudo pip3 install -r CarpMasterV2_0/requirements.txt

# This line installs all needed packages
#SAM NEEDS TO CHECK THIS WORKS ON NEW RPI
cat requirements.txt | xargs sudo apt-get install

#Next make sure that all hardware is installed correctly.


python3 app.py


#You will need to find the serial numbers of all DSB1820 sensors.

# Add OneWire support
sudo nano /boot/config.txt

#scroll to bottom of the file and add the following:

    # Following line added by [name] on [date] for temperature sensor
dtoverlay=w1-gpio

#restart pi
sudo reboot

#run the following commands
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls
# At this point you should see one or more entries of the form: cd 28-xxxx, each corresponding to one sensor.