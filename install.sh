DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
#Install rainbow www.github.com/bqlabs/rainbow

sudo apt-get install python-dev libzmq3-dev avahi-daemon

# Disable avahi on init
sudo update-rc.d -f avahi-daemon remove

sudo pip install pyrainbow


#Install slic3r

sudo apt-get install slic3r

#Uninstall old Sunrise server
sudo rm -r /opt/sunrise

#Install current Sunrise server
sudo mkdir /opt/sunrise
sudo cp -r ./src/* /opt/sunrise/

sudo sed -i -e '$i \sudo chmod 777 "/dev/ttyAMA0"\n\r /usr/bin/python /opt/sunrise/sunrise_server.py \n' ~/.config/lxsession/LXDE-pi/autostart
