import subprocess
from rainbow import register


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

    @register
    def sliceFile(name='name', content='content'):
        try:
            os.mkdir('temp')
        except Exception:
            pass
        temp_stl_path=os.path.join(os.getcwd(),'temp','loaded.stl')
        print temp_stl_path
        with open(temp_stl_path, 'w') as file_:
            file_.write(base64.b64decode(content))
            self.file_to_svg(temp_stl_path,50)
            response = name + " successfully sliced"
            return response
