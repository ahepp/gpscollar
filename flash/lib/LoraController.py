from network import LoRa
import ubinascii

class LoraController:
    def __init__():
        self._lora = LoRa(mode=LoRa.LORAWAN)

    def canSend(self):
        """return true if interface can send data, false otherwise"""
        return False

    def send(self, data):
        """attempts to send via interface, returns success status"""
        return False
