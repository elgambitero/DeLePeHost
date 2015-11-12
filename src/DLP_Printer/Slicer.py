import subprocess


class Slicer(object):
    def __init__(self):
        #I may want to check if Slic3r is installed
        return

    def file_to_svg(self,filepath,layerHeight):
        print filepath
        command= "./" + str(filepath) + " --export-svg " + "--layer-height " + str(layerHeight/1000.0) + " --output ./temp/loaded_" + str(layerHeight) + ".svg"
        print command
        subprocess.call(["slic3r", command])
