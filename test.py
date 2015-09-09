from DLP_Printer import DLP_Printer

file = open("./thing.3dlp")

sunrise = DLP_Printer()

def printProcess():
    sunrise = Sunrise()
    sunrise.projCalibration()
    sunrise.homeAxis()
    sunrise.buildPrint()


print(sunrise.Zaxis.moveAxis(50, 200, relative=True))