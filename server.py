#!/usr/bin/env python

from rainbow import register, publish, run
from mechComm import mechComm



@register('startMechBoard')
def startMechBoard():
    global mio
    mio = mechComm()
    publish("connected!","texto")
    if mio is None:
        return "Error when connecting."
    else:
        return "Success connecting to board."

@register('moveAxis')
def moveAxis(amount):
    global mio
    a='G1 Y' + str(amount) + ' F200 \n\r'
    mio.write('G91\n\r')
    mio.write(a)
    response='Moving Y axis by ' + str(amount) + ' mm.'
    return response

run(host='0.0.0.0', webserver=True)
