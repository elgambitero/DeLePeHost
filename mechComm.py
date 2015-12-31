# -*- coding: utf-8 -*-
# This file is part of the Sunrise Project

__author__ = 'Jaime García Villena <elgambitero@gmail.com>'
__copyright__ = 'Copyright (C) 2015-2016 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'


import serial
import glob
import time

class mechComm(serial):

    def __init__(self):
        self.myport='error'
        self.connected=False
        ports=[]
        for device in ['/dev/ttyAMA*','/dev/ttyACM*', '/dev/ttyUSB*', '/dev/tty.usb*', '/dev/tty.wchusb*',
                           '/dev/cu.*', '/dev/rfcomm*']:
            ports = ports + glob.glob(device)
        print(">>> Finding a valid GRBL controller board...")
        print(ports)
        for port in ports:
            super(mechComm,self).__init__(port, 115200, timeout=2)
            time.sleep(4)
            self.version = self.getData()
            if "Grbl 0.9j ['$' for help]" in self.version:
                self.myport=port
                print(">>> Success!")
                self.connected=True
                break
        if self.myport=='error':
            print(">>> Could not find GRBL controller")
        return

    def getData(self):
        if self.isOpen():
            out = ''
            while self.inWaiting() > 0:
                out += self.read(1)
        return out

    def _reset(self):
        self.setDTR(False)
        time.sleep(0.022)
        self.flushInput()
        self.flushOutput()
        self.setDTR(True)
        #self.getData()

    def moveAxis(self,axis,distance,speed):
        if self.connected is True:
            self.write("G91\n\r" + "G1 " + axis + str(distance) + " F" + str(speed))
        else
            print("Err: controller not connected")
