import MechComm
import wx
import subprocess
import time

class Projector(object):

    def __init__(self, resolution, pixel_sizes, proj_axis, MechComm):

        #Projector has said resolution:

        self._resolution = resolution

        #It's able to print in these pixel ranges.
        self._pixel_sizes = pixel_sizes;

        if type(proj_axis)==str:
            self._proj_axis = proj_axis

        self.start_display()



    def calibrate(self):
        # TODO
        return False

    def set_pixel_size(PixelSize):
        # TODO
        return False

    def start_display(self):
        print "Iniciando server X"
        #subprocess.Popen("startx",shell=True)
        time.sleep(8)
        print "Iniciando App wx"
        app=wx.App()
        frame=wx.Frame(None,wx.ID_ANY,"proyector")
        frame.SetBackgroundColour("black")
        frame.ShowFullscreen(True)
        frame.Show(True)
        app.MainLoop()
