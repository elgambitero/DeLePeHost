import MechComm
import subprocess
import threading


class Projector(object):

    def __init__(self, pixel_sizes, proj_axis, MechComm):
        #It's able to print in these pixel ranges.
        self._pixel_sizes = pixel_sizes;
        self._pixel_size = _pixel_sizes[1]

        #Has, or not, an axis that controls it's distance to the VAT
        self._proj_axis = proj_axis

        #Get projector resolution
        self.get_resolution()

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

    def blank():
        d.blank()

    def get_resolution(self):
        cmd = ['xrandr']
        cmd2 = ['grep', '*']
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
        p.stdout.close()
        resolution_string, junk = p2.communicate()
        resolution = resolution_string.split()[0]
        width, height = resolution.split('x')
        self._resolution=[int(width), int(height)]
        print "Projector resolution is. " + str(self._resolution[0]) + "x" + str(self._resolution[1])
