import Mechanical.MechComm as MechComm
import Slicer.Slicer as Slicer
import Projector.Projector as Projector
import display as d
import time
import threading
from rainbow import publish


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

        self.building = False

    def buildBegin(self,filename,params):
        self.building = True
        print filename
        model=self.slicer.parseSVG(filename)
        t = threading.Thread(target=self.buildLoop, args=(model,params))
        t.daemon = True
        t.start()
        publish('printStarted','Build began')
        return "Begin printing"



    def buildLoop(self,model,params):
        self.projector.init_display()
        for layer in model:
            if not self.building:
                break
            publish('printingLayer',len(layer))
            self.projector.expose(layer)
            time.sleep(params['exposeTime'])
            self.projector.blank()
            self.mechComm.moveAxis(self.buildAxis,3,200)
            self.mechComm.moveAxis(self.buildAxis,-2.95,200)
            time.sleep(params['blankTime'])
        self.mechComm.moveAxis(self.buildAxis,20,200)
        publish('printFinished',"Build finished")
        return False

    def cancelBuild(self):
        self.building = False
