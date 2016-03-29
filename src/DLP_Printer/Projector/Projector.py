from ..Mechanical import MechComm
import subprocess
import threading
import display as d

class Projector(object):

    def __init__(self, pixel_sizes, proj_axis, MechComm):
        #It's able to print in these pixel ranges.
        self._pixel_sizes = pixel_sizes;
        self._pixel_size = pixel_sizes[1]

        #Has, or not, an axis that controls it's distance to the VAT
        self._proj_axis = proj_axis

        #Start display thread
        self.init_display()


    def calibration(self):
        #TODO
        return False

    def set_pixel_size(PixelSize):
        # TODO
        return False

    def init_display(self):
        d.init()
        return

    def expose(layer):
        d.expose(layer)

    def blank(self):
        d.blank()
