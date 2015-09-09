from sunrise import Sunrise

file = open(thing.3dlp)

sunrise = Sunrise()
sunrise.ProjCalib()
sunrise.HomeAxis()
sunrise.Print(file)
