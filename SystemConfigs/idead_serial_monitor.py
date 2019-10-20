#!/usr/local/opt/python/bin/python3.7

import re
import serial
from serial.tools import list_ports
from datetime import date
from datetime import time
from datetime import datetime

button = None

while True:
    ports = serial.tools.list_ports.comports(include_links=False)
    
    for port in ports:
        pattern = 'usbmodem'
        if re.search(pattern, port.device):
            button = port

    if button is not None:
        break

ser = serial.Serial(button.device)
serinput = ser.read(100)
if re.search(b'yes',serinput):
    log = open("idead.log","a+")
    now = datetime.now()
    log.write("\n%s: Button Pressed" % now.strftime("%c"))
