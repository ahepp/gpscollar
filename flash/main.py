# Pycom libs
from pytrack import Pytrack
from L76GNSS import L76GNSS

# Micropython libs
import usocket
import ustruct
import utime

# Interface controllers
from WifiController import WifiController
#from LteController import LteController

# ---- Initialize constants ----
#url = "whereischarlie.org"
delay = 1000

# ---- Initialize Pytrack and GPS ----
py  = Pytrack()
gps = L76GNSS(py, timeout=30)

# ---- Initialize WiFi interface ----
wifi = WifiController()

# ---- Mainline ----
while True:
    # set deadline
    deadline = utime.ticks_ms() + delay

    (lat, lng) = gps.coordinates()
    if (lat != None) and (lng != None): # wait for gps fix
        if wifi.canSend():
            data = bytearray(ustruct.pack("ff", lat, lng)) #TODO byte order?
            wifi.send(data)

    # sleep until deadline
    dur = deadline - utime.ticks_ms()
    if dur > delay: # handles rollover by not waiting at all
        utime.sleep_ms(dur)
