import machine
import time

from network import WLAN

ADDR='192.168.1.100'
SUBNET_MASK='255.255.255.0'
DEFAULT_GATEWAY='192.168.1.1'
DNS_SERVER='8.8.8.8'

class WifiController:
    def __init__(self):
        self._wlan = WLAN(mode=WLAN.STA)
        nets = self._wlan.scan()
        for net in nets:
            if net.ssid == 'stranger':
                self._wlan.connect(net.ssid, auth=(WLAN.WPA2, 'inastrangewlan'), timeout=5000)
                while not self._wlan.isconnected():
                    machine.idle()
                break
        self._wlan.ifconfig(config=(ADDR, SUBNET_MASK, DEFAULT_GATEWAY, DNS_SERVER))

    def canSend(self):
        """return true if interface can send data, false otherwise"""
        return self._wlan.isconnected()

    def send(self, data):
        """attempts to send via interface, returns success status"""
        return False
