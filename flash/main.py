# Pycom libs
from pytrack import Pytrack
from L76GNSS import L76GNSS

import os
from machine import SD

# Micropython libs
import usocket
import ustruct
import utime

# Interface controllers
from WifiController import WifiController

# ---- Initialize constants ----
delay_ms = 100
log_writeback_cnt = 1

# ---- Initialize Pytrack and GPS ----
py  = Pytrack()
gps = L76GNSS(py, timeout=30)
sd = SD()
os.mount(sd, '/sd')
f = open('/sd/log.txt', 'a')

# ---- Initialize WiFi interface ----
wifi = WifiController()

# ---- Mainline ----
cnt = 0
while True:
    # set deadline
    deadline = utime.ticks_ms() + delay_ms

    # get data and log it
    coords = gps.coordinates()
    time = gps.getUTCTime()
    lat = coords['latitude']
    lng = coords['longitude']

    f.write(time + ", " + str(lat) + ", " + str(lng) + "\n")
    print(time)
    print(lat)
    print(lng)
    cnt = cnt + 1
    if cnt > log_writeback_cnt:
        f.close()
        f = open('/sd/log.txt', 'a')
        cnt = 0

    if wifi.canSend():
        # marshal data and send it
        try:
            data = bytearray(ustruct.pack("ff", lat, lng))
        except TypeError:
            print(lat)
            print(lng)
        wifi.send(data)
    else:
        wifi.connect()

    # sleep until deadline
    dur = deadline - utime.ticks_ms()
    if dur > delay_ms: # handles rollover by not waiting at all
        utime.sleep_ms(dur)
