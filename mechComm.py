# -*- coding: utf-8 -*-
# This file is part of the Sunrise Project

__author__ = 'Jaime García Villena <elgambitero@gmail.com>'
__copyright__ = 'Copyright (C) 2015-2016 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'


import serial
import glob
import time

class mechComm():

    def __init__(self):
        self.myport='error'
        ports=[]
        for device in ['/dev/ttyAMA*','/dev/ttyACM*', '/dev/ttyUSB*', '/dev/tty.usb*', '/dev/tty.wchusb*',
                           '/dev/cu.*', '/dev/rfcomm*']:
            ports = ports + glob.glob(device)
        print(">>> Finding a valid GRBL controller board...")
        print(ports)
        for port in ports:
        #try:
            self.serial = serial.Serial(port, 115200, timeout=2)
            time.sleep(4)
            if self.serial.isOpen():
                print(">>> Found "+ port+ " open...")
                self.serial.write("\x18\n\r")
                time.sleep(4)
                self.version = self.getData()
                if "Grbl 0.9j ['$' for help]" in self.version:
                    self.myport=port
                    print(">>> Success!")
                    break
            #else:
            #    self.serial.close()
        #except:
        #    pass
        if self.myport=='error':
            print(">>> Could not find GRBL controller")
        return

    def getData(self):
        if self.serial.isOpen():
            out = ''
            while self.serial.inWaiting() > 0:
                out += self.serial.read(1)
        return out


    def write(self,string):
        self.serial.write(string)

    def _reset(self):
        self.serial.setDTR(False)
        time.sleep(0.022)
        self.serial.flushInput()
        self.serial.flushOutput()
        self.serial.setDTR(True)
        #self.getData()
