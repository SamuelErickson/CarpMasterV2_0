To set up this package on a Raspberry pi, run the following lines:

#First, set up a virtual environment for code to execute in
sudo pip3 install virtualenv
virtualenv -p python3 myenv

# Download all needed code from github
git clone https://github.com/SamuelErickson/CarpMasterV2_0.git
sudo pip3 install -r CarpMasterV2_0/requirements.txt

# This line installs all needed packages
python3 app.py