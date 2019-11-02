# Pycom libs
from pytrack import Pytrack
from L76GNSS import L76GNSS

# Micropython libs
import json
import time
import urequests

# Interface controllers
from WifiController import WifiController

# ---- Initialize constants ----
url = "https://whereischarlie.org/position"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
delay = 1000

# ---- Initialize Pytrack and GPS ----
py  = Pytrack()
gps = L76GNSS(py, timeout=30)

# ---- Initialize WiFi interface ----
wifi = WifiController()

# ---- Mainline ----
while True:
    deadline = time.ticks_ms() + delay # should fail gracefully on rollover
    (lat, lng) = gps.coordinates()
    data = {'lat': lat, 'lng': lng}
    #print("(" + str(lat) + ", " + str(lng) + ")")
    if (lat != None) and (lng != None):
        r = urequests.post(url, data=json.dumps(data), headers=headers)
    dur = deadline - time.ticks_ms()
    if dur > 0:
        time.sleep_ms(dur)
