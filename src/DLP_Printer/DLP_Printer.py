import Mechanical.MechComm
import Slicer.Slicer
import Projector.Projector

class DLP_Printer(object):

    def __init__(self,ProjAxis='X'):


        # Let's connect to the mechanical controller
        self.mechComm = MechComm.MechComm()

        # The Sunrise has one axis, the platform. We call it Y.
        self.buildAxis="Y"

        # It has a projector with a 1280x800 resolution. It is mounted on a
        # carriage that allows continous pixel sizes from 45 um, to 70 um. That
        #axis is called X.
        self.Projector = Projector.Projector(('continous', 40, 70), "X", self.mechComm)

        #
        self.slicer = Slicer.Slicer()


    def buildPrint(file):
        # TODO
        return False
