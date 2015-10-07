import serial
import glob
import time

class mechComm():

    def __init__(self):
        self.myport='a'
        ports = glob.glob('/dev/tty[A-Za-z]*')
        for port in ports:
            try:
                self.serial = serial.Serial()
                self.serial.port = port
                self.serial.baudrate = 115200
                if self.serial.isOpen:
                    self.myport=port
                    break
                else:
                    self.serial.close()
            except:
                pass
        return

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

    def write(self,string)
        self.serial.write(string)
