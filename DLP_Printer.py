import mechanical
import projector
import serialHandler as serial


class DLP_Printer(object):

    def __init__(self,ProjAxis='X'):

    	self.mechComm = serial.SerialConnection('/dev/ttyACM10')


        # The Sunrise has one axis, the platform. We call it Z.

        self.Zaxis = mechanical.Axis('Z',self.mechComm)

        # And it has a projector with a 1280x800 resolution. It is mounted on a
        # carriage that allows continous pixel sizes from 45 um, to 70 um. That axis is
        # called X.

        self.Projector = projector.Projector(
            (1280, 800), ('continous', 45, 70), ProjAxis, self.mechComm)

    def projCalibrate(self):
        # TODO
        return False

    def homeAxis(self):
        # TODO
        return False

    def buildPrint(file):
        # TODO
        return False

    def setPixelSize(PixelSize):
        # TODO
        return False
