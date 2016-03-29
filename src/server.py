#!/usr/bin/env python

from rainbow import register, publish, run
from DLP_Printer.DLP_Printer import DLP_Printer
import os.path



@register
def save_file(name='name', content='content'):
    with open(name, 'w') as file_:
        import base64
        file_.write(base64.b64decode(content))
        return "OK"


if __name__ == '__main__':
    sunrise=DLP_Printer()
    try:
        os.rmdir("./temp")
    except:
        pass

    run(host='0.0.0.0', webserver=True)
