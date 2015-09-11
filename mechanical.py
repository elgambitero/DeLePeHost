
class Axis(object):

    def __init__(self, letter, mechComm):
        if letter in 'XYZ':
            self.letter = letter
            self.mechComm = mechComm
        else:
            raise

    def move(self, distance, speed, relative):
        move = 'G1 '+self.letter+str(distance)+' F'+str(speed)+'\n'
        if relative:
            self.mechComm.write('G91\n'+move+'G90\n')
        else:
            self.mechComm.write(move)

    def setStepsPermm(self, steps):
        if self.letter == 'X':
            code = 100
        elif self.letter == 'Y':
            code = 101
        elif self.letter == 'Z':
            code = 102
        else:
            return False
        self.mechComm.write('$'+str(code)+'='+str(steps)+'\n')
        return True
