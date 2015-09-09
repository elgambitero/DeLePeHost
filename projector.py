import mechanical

class Projector(object):

	def __init__(self, resolution, pixelSizes, ProjAxis, mechComm):

		#Projector has said resolution:

		self. Resolution = resolution

		#It's able to print in these pixel ranges.
		self. pixelSizes = pixelSizes;

		if type(ProjAxis)==str:
			self.Axis = mechanical.Axis(ProjAxis,mechComm)