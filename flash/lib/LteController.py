from network import LTE
import time

class LteController:
    def __init__(self):
        self._lte = LTE()
        self._lte.attach()
        while not self._lte.isattached():
            time.sleep(1)
        self._lte.connect()
        while not self._lte.isconnected():
            time.sleep(1)
        print(self._lte.isattached())
        print(self._lte.isconnected())

    def canSend(self):
        """return true if interface can send data, false otherwise"""
        return self._lte.isconnected()

    def send(self, data):
        """attempts to send via interface, returns success status"""
        return False
