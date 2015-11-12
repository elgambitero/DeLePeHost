#!/usr/bin/env python

from rainbow import register, publish, run
from DLP_Printer.DLP_Printer import DLP_Printer
import os.path

sunrise=DLP_Printer()
try:
    os.rmdir("./temp")
except:
    pass

import base64


@register
def save_file(name='name', content='content'):
    with open(name, 'w') as file_:
        file_.write(base64.b64decode(content))
        return "OK"


@register
def moveAxis(amount=0):
    a='G1 Y' + str(amount) + ' F200 \n\r'
    sunrise.mechComm.write('G91\n\r')
    sunrise.mechComm.write(a)
    response='Moving Y axis by ' + str(amount) + ' mm.'
    return response

@register
def unlockMech():
    sunrise.mechComm.write("$x\r\n")
    answer = sunrise.mechComm.getData();
    if "ok" in answer:
        return "Alarm lock successfully released"
    else:
        return "ERROR: Communication could't be established with cnc board"

@register
def sliceFile(name='name', content='content'):
    try:
        os.mkdir('temp')
    except Exception:
        pass
    temp_stl_path=os.path.join('temp','loaded.stl')
    print temp_stl_path
    with open(temp_stl_path, 'w') as file_:
        file_.write(base64.b64decode(content))
        sunrise.slicer.file_to_svg(temp_stl_path,50)
    response = name + " successfully sliced"
    return response


run(host='0.0.0.0', webserver=True)
