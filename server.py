#!/usr/bin/env python

from bottle import route, run
from mechComm import mechComm

mio=mechComm()


@route('/moveAxis/<amount>')
def moveAxis(amount):
    a='G1 Y' + amount + ' F200 \n\r'
    mio.write('G91\n\r')
    mio.write(a)
    response='Moving Y axis by ' + amount + ' mm.'
    return response

run(host='172.16.17.102', port=8082)
