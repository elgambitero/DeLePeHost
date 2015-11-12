import MechComm

class Projector(object):

    def __init__(self, resolution, pixel_sizes, proj_axis, MechComm):

        #Projector has said resolution:

        self._resolution = resolution

        #It's able to print in these pixel ranges.
        self._pixel_sizes = pixel_sizes;

        if type(proj_axis)==str:
            self._proj_axis = proj_axis


    def calibrate(self):
        # TODO
        return False

    def set_pixel_size(PixelSize):
        # TODO
        return False
