import subprocess


class Slicer(object):
    def __init__(self):
        #I may want to check if Slic3r is installed
        return

    def file_to_svg(self,filename,layerHeight):
        outfile = filename[:-4] + ".svg"
        command = filename + " --export-svg " + "--layer-height " + str(layerHeight/1000.0) + " --output " + outfile
        print command
        if subprocess.Popen("slic3r " + command,shell=True) is 0:
            return outfile
        else:
            return False
