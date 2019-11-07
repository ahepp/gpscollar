from network import LoRa
import struct
import ubinascii
import usocket
import utime


class LoraController:
    def __init__(self):
        self._lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

        # create an ABP authentication params
        app_eui = ubinascii.unhexlify('70B3D57ED0024EC6')
        app_key = ubinascii.unhexlify('FDFB753170AF61970D3D0B0896697698')

        # join a network using ABP (Activation By Personalisation)
        self._lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
        while not self._lora.has_joined():
            utime.sleep(2)
            print("not yet joined...")

        # create a LoRa socket
        s = usocket.socket(usocket.AF_LORA, usocket.SOCK_RAW)

        # set the LoRaWAN data rate
        s.setsockopt(usocket.SOL_LORA, usocket.SO_DR, 5)

        # send some data
        s.send(bytes([0x01, 0x02, 0x03]))

    def canSend(self):
        """return true if interface can send data, false otherwise"""
        return True

    def send(self, data):
        """attempts to send via interface, returns success status"""
        return False
