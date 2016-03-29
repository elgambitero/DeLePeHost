DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
#Install rainbow www.github.com/bqlabs/rainbow

sudo apt-get install -y python-dev libzmq3-dev avahi-daemon --fix-missing

# Disable avahi on init
sudo update-rc.d -f avahi-daemon remove

sudo pip install -y pyrainbow


#Install slic3r

sudo apt-get install -y slic3r --fix-missing



#Uninstall old Sunrise server
sudo rm -r /opt/sunrise

#Install current Sunrise server
sudo mkdir /opt/sunrise
sudo cp -r ./src/* /opt/sunrise/

#Install ajstark's openvg libraries
cd $DIR
cd ..
git clone https://github.com/elgambitero/openvg.git
cd openvg
sudo apt-get install -v libjpeg8-dev indent libfreetype6-dev ttf-dejavu-core
make library
sudo make install

#Install display python module
cd $DIR
cd src/DLP_Printer/Projector
sudo python setup.py install


sudo sed -i -e '$i /usr/bin/python /opt/sunrise/sunrise_server.py \n' /etc/rc.local

#Put USER into dialout group
sudo usermod -a -G dialout $USER

#Reboot system
sudo reboot
