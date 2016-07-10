
import subprocess
import xml.etree.ElementTree as ET


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

    def parseSVG(self,filename,pixel):
        print "Try to parse"
        tree = ET.parse(filename)
        root = tree.getroot()
        model=()
        size=(float(root.attrib['width']),float(root.attrib['height']))


        for layer in root:
            laytuple=()

            for contour in layer:
                contuple=()
        #        print(contour.attrib['{http://slic3r.org/namespaces/slic3r}type'])
                if contour.attrib['{http://slic3r.org/namespaces/slic3r}type'] == 'contour':
                    contuple=contuple+(1,)
                elif contour.attrib['{http://slic3r.org/namespaces/slic3r}type'] == 'hole':
                    contuple=contuple+(0,)
                coordinates=contour.attrib['points'].split()

                Xlist=[]
                Ylist=[]

                for coordinate in coordinates:
                    Xlist.append(float(coordinate.split(',')[0]))
                    Ylist.append(float(coordinate.split(',')[1]))

        	#HARDCODE a resize for 40 micron pixels
                XlistCorr=[640+(1000.0/pixel)*(x-size[0]/2) for x in Xlist]
                YlistCorr=[400+(1000.0/pixel)*(x-size[1]/2) for x in Ylist]

                contuple = contuple + (XlistCorr,)
                contuple = contuple + (YlistCorr,)
                print(len(Xlist))
                laytuple = laytuple + (contuple,)
            model = model + (laytuple,)
        return model
