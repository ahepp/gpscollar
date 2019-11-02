# Pycom libs
from pytrack import Pytrack
from L76GNSS import L76GNSS

# Micropython libs
import json
import time
import urequests

# Custom libs
import Handler
import LoraController
import LteController
import WifiController


# ---- Initialize constants ----
#url = "https://whereischarlie.org/position"
url = "https://test.default.whereischarlie.appspot.com/position"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
delay = .1

# ---- Initialize Pytrack and GPS ----
py  = Pytrack()
gps = L76GNSS(py, timeout=30)

# ---- Initialize communication controllers ----
#lora = LoraController()
#wifi = WifiController()
#lte  = LteController()

# ---- Initialize connection handler ----
#handler = Handler()
#handler.registerCommIf(lora)
#handler.registerCommIf(wifi)
#handler.registerCommIf(lte)

# ---- Mainline ----
while True:
    #handler.send()
    (lat, lng) = gps.coordinates()
    data = {'lat': lat, 'lng': lng}
    if (lat != None) and (lng != None):
        r = urequests.post(url, data=json.dumps(data), headers=headers)
    time.sleep(delay)
