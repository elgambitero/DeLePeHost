#from DLP_Printer import DLP_Printer

#file = open("./thing.3dlp")

#sunrise = DLP_Printer()

#def printProcess():
#    sunrise = Sunrise()
#    sunrise.projCalibration()
#    sunrise.homeAxis()
#    sunrise.buildPrint()


#sunrise.Zaxis.move(-30, 200, relative=True)

from sunrise.MechComm import MechComm

mio=MechComm()
print(mio.myport)
