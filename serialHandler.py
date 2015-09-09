#-----------------------------------------------------------------------#
#                                                                       #
# This function is part of the web2board project                            #
#                                                                       #
# Copyright (C) 2015 Mundo Reader S.L.                                  #
#                                                                       #
# Date: August 2015                                                     #
# Author: Irene Sanz Nieto <irene.sanz@bq.com>                          #
#                                                                       #
#-----------------------------------------------------------------------#

import serial
import time


class SerialConnection():

    def __init__(self, port):
        self.serial = serial.Serial()
        self.serial.port = port
        self.serial.baudrate = 115200
        self.serial.open()
    	self.changeBaudRate(115200)
    	self.write('$$')
    	while 1:
            data = self.getData()
            if data is not None and 'Grbl 0.9j' in data:
                break



    def getData(self):
        if self.serial.isOpen():
            out = ''
            try:
                while self.serial.inWaiting() > 0:
                    out += self.serial.read(1)
                if out != '':
                    return out
            except:
                pass

    def write(self, data):
        self.serial.write(data.encode())

    def changeBaudRate(self, value):
        self.serial.close()
        self.serial.baudrate = value
        self.serial.open()

    def close(self):
        self.serial.close()
