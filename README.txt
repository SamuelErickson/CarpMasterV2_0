To set up this package on a Raspberry pi, run the following lines:

#First, set up a virtual environment for code to execute in
sudo pip3 install virtualenv
virtualenv -p python3 myenv

# Download all needed code from github
git clone https://github.com/SamuelErickson/CarpMasterV2_0.git
sudo pip3 install -r CarpMasterV2_0/requirements.txt

# This line installs all needed packages
python3 app.py

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
cd 28-xxxx (change this to match what serial number pops up)
cat w1_slave