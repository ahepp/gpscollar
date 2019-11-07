import os
import machine
from machine import SD
from machine import Timer

import usocket
import ustruct
import utime

from pytrack import Pytrack
from L76GNSS import L76GNSS

from WifiController import WifiController

def log_coords(alarm):
    global lat
    global lng
    global log

    print("log_coords")
    (llat, llng) = gps.coordinates()

    irq_state = machine.disable_irq()
    lat = llat
    lng = llng
    if not ((lat == None ) or (lng == None)):
        log = log + str(utime.ticks_ms()) + ", " + str(lat) + ", " + str(lng) + "\n"
    machine.enable_irq(irq_state)
    print("end log_coords")

def log_wb(alarm):
    global log

    print("log_wb")

    irq_state = machine.disable_irq()
    llog = log
    log = ""
    machine.enable_irq(irq_state)

    f = open('/sd/log.txt', 'a')
    f.write(llog)
    f.close()

    print("end log_wb")

def udp_send(alarm):
    global lat
    global lng

    print("udp_send")

    irq_state = machine.disable_irq()
    llat = lat
    llng = lng
    machine.enable_irq(irq_state)

    print (llat)
    print (llng)

    if not ((llat == None ) or (llng == None)):
        if wifi.canSend():
            data = bytearray(ustruct.pack("ff", float(llat), float(llng)))
            wifi.send(data)
            print("sent!")
        else:
            wifi.connect()
    print("end udp_send")

py  = Pytrack()
gps = L76GNSS(py)

print("initializing wifi")
wifi = WifiController()

print("mounting sd")
sd = SD()
os.mount(sd, '/sd')

lat = None
lng = None
log = ""

udp_send_interval_ms = 10
log_interval_ms = 1
log_wb_interval_ms = 10

print("configuring callbacks")
Timer.Alarm(log_coords, 1, periodic=True)
Timer.Alarm(log_wb, 5, periodic=True)
Timer.Alarm(udp_send, 10, periodic=True)

print("entering mainline")
while True:
    machine.idle()
