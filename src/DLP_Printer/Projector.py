import MechComm
import wx
import subprocess
import threading
import time

class Projector(object):

    def __init__(self, pixel_sizes, proj_axis, MechComm):
        #It's able to print in these pixel ranges.
        self._pixel_sizes = pixel_sizes;

        #Has, or not, an axis that controls it's distance to the VAT
        self._proj_axis = proj_axis

        #Start controlling the display
        self.start_display()



    def calibrate(self):
        # TODO
        return False

    def set_pixel_size(PixelSize):
        # TODO
        return False

    def start_display(self):
        print "Iniciando App wx"
        app=wx.App()
        self.resolution = wx.GetDisplaySize()
        frame=wx.Frame(None,wx.ID_ANY,"proyector")
        frame.SetBackgroundColour("black")
        frame.ShowFullScreen(True)
        frame.Show(True)
        cursor = wx.StockCursor(wx.CURSOR_BLANK)
        frame.SetCursor(cursor)
        self.thread = threading.Thread(target=app.MainLoop)
        self.thread.setDaemon(1)
        self.thread.start()
