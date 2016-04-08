# -*- coding: utf-8 -*-
# This file is part of the Sunrise Project

__author__ = 'Jaime García Villena <elgambitero@gmail.com>'
__copyright__ = 'Copyright (C) 2015-2016 Mundo Reader S.L.'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'


import serial
import glob
import time

class MechComm(serial.Serial):

    def __init__(self):
        self.myport='error'
        self.connected=False
        ports=[]
        for device in ['/dev/ttyAMA*','/dev/ttyACM*', '/dev/ttyUSB*',
            '/dev/tty.usb*', '/dev/tty.wchusb*','/dev/cu.*', '/dev/rfcomm*']:
            ports = ports + glob.glob(device)
        print(">>> Finding a valid GRBL controller board...")
        print(ports)
        for port in ports:
            super(MechComm,self).__init__(port, 115200, timeout=2)
            self._ctrlXReset()
            self._DTRReset()
            time.sleep(3)
            for i in xrange(3):
                self.version = self.getData()
                if self.checkVersion():
                    self.myport=port
                    print(">>> Success! GRBL Board found at port: "+port)
                    break
        if self.myport=='error':
            print(">>> Could not find GRBL controller")
        return


    def checkVersion(self):
        print self.version
        if "Grbl 0.9j ['$' for help]" in self.version:
            self.connected=True
            return True
        else:
            return False

#Courtesy of Irene Sanz Nieto <irene.sanz@bq.com> from web2board project
    def getData(self):
        if self.isOpen():
            out = ''
            while self.inWaiting() > 0:
                out += self.read(1)
        return out

    def _DTRReset(self):
        self.setDTR(False)
        time.sleep(0.022)
        self.flushInput()
        self.flushOutput()
        self.setDTR(True)
        #self.getData()

    def _ctrlXReset(self):
        self.write("\x18\r\n")

    def moveAxis(self,axis,distance,speed):
        if self.connected:
            self.write("G91\n\r" + "G1 " + axis + str(distance) + " F" +
                str(speed) + "\n\r")
        else:
            print("Err: controller not connected")

    def homeAxis(self):
        if self.connected:
            self.write("$H\n\r")
        else:
            print("Err: controller not connected")
        return False

    def setStepsPermm(self, axis, steps):
        if axis == 'X':
            code = 100
        elif axis == 'Y':
            code = 101
        elif axis == 'Z':
            code = 102
        else:
            return False
        self.write('$'+str(code)+'='+str(steps)+'\n')
        return True

    def wakeUp(self):
        while 1:
            data = self.getData()
            if data is not None and 'Grbl 0.9j' in data:
                print(data)
                break
