# Micropython libs
import logging

# Pycom libs
from pytrack import Pytrack

# 3rd party libs for pycom modules
from L76GNSSV4 import L76GNSS

# Custom libs
import Handler
import LoraController
import LteController
import Serializer
import WifiController


# ---- Initialize constants ----

# ---- Initialize logger ----
logger = logging.getLogger("logger")

# ---- Initialize Pytrack and GPS ----
py  = Pytrack()
gps = L76GNSS(py, timeout=30)

# ---- Initialize communication controllers ----
lora = LoraController()
wifi = WifiController()
lte  = LteController()

# ---- Initialize Serializer ----
serializer = Serializer()

# ---- Initialize connection handler ----
handler = Handler()
handler.registerDataCallback(serilizer.serialize(gps.coor))
handler.registerCommIf(lora)
handler.registerCommIf(wifi)
handler.registerCommIf(lte)

# ---- Mainline ----
while True:
    logger.debug("calling handler.send()")
    handler.send(serilizer.serialize(gps.coordinates()))
    logger.debug("calling sleep for 1s")
    time.sleep_ms(1000)
