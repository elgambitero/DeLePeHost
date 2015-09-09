
class Axis(object):

    def __init__(self, letter, mechComm):
        self.letter = letter
        self.mechComm = mechComm

    def moveAxis(self, distance, speed, relative):
        # TODO
        self.mechComm.write('G91\n')
        self.mechComm.write('G1 Z-80 F500\n')
        self.mechComm.write('G90\n')
        return 'a'

    def setStepsPermm(self, steps):
        # TODO
        return False

