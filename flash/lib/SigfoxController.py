from network import Sigfox
import struct
import ubinascii
import usocket
import utime


class SigfoxController:
    def __init__(self):
        self._sigfox= Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ2)

        s = usocket.socket(usocket.AF_SIGFOX, usocket.SOCK_RAW)

        s.setblocking(True)

        s.setsockopt(usocket.SOL_SIGFOX, usocket.SO_RX, False)

        s.send(bytes([0x01, 0x02, 0x03]))

    def canSend(self):
        """return true if interface can send data, false otherwise"""
        return False

    def send(self, data):
        """attempts to send via interface, returns success status"""
        return False
