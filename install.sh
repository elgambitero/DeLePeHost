DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
#Install rainbow www.github.com/bqlabs/rainbow

sudo apt-get install python-dev libzmq3-dev avahi-daemon --fix-missing

# Disable avahi on init
sudo update-rc.d -f avahi-daemon remove

sudo pip install pyrainbow


#Install slic3r

sudo apt-get install slic3r --fix-missing

#Uninstall old Sunrise server
sudo rm -r /opt/sunrise

#Install current Sunrise server
sudo mkdir /opt/sunrise
sudo cp -r ./src/* /opt/sunrise/

#Put USER in dialout group
sudo usermod -a -G dialout $USER
