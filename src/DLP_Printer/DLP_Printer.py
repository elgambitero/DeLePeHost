import Mechanical.MechComm as MechComm
import Slicer.Slicer as Slicer
import Projector.Projector as Projector
import display as d
import time

class DLP_Printer(object):

    def __init__(self,ProjAxis='X'):


        # Let's connect to the mechanical controller
        self.mechComm = MechComm.MechComm()

        # The Sunrise has one axis, the platform. We call it Y.
        self.buildAxis="Y"

        # It has a projector with a 1280x800 resolution. It is mounted on a
        # carriage that allows continous pixel sizes from 45 um, to 70 um. That
        #axis is called X.
        self.projector = Projector.Projector(('continous', 40, 70), "X", self.mechComm)

        #
        self.slicer = Slicer.Slicer()


    def buildPrint(self,filename,params):
        model=self.slicer.parseSVG(filename)
        self.mechComm.homeAxis()
        for layer in model:
            self.projector.expose(layer)
            time.sleep(params['exposeTime'])
            self.projector.blank()
            time.sleep(params['blankTime'])
            self.mechComm.moveAxis(self.buildAxis,3,200)
            self.mechComm.moveAxis(self.buildAxis,-2.95,200)
            time.sleep(1000)
        self.mechComm.moveAxis(self.buildAxis,20,200)
        return False
