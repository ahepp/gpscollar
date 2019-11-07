import machine
import usocket

from network import WLAN

CONNECTION_TIMEOUT_MS = 5000

url="35.239.96.98"
port=5000
ADDR='192.168.1.100'
SUBNET_MASK='255.255.255.0'
DEFAULT_GATEWAY='192.168.1.1'
DNS_SERVER='8.8.8.8'

class WifiController:
    def __init__(self):
        self._wlan = WLAN(mode=WLAN.STA)
        self.connect()
        self._wlan.ifconfig(config=(ADDR, SUBNET_MASK, DEFAULT_GATEWAY, DNS_SERVER))
        self._sock = self.makeSock()

    def connect(self):
        """connect to wifi"""
        self._wlan.connect('stranger', auth=(WLAN.WPA2, 'inastrangewlan'), timeout=CONNECTION_TIMEOUT_MS)

    def makeSock(self):
        # Open up a UDP socket to our target
        ai = usocket.getaddrinfo(url, port)
        s = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM, usocket.IPPROTO_UDP)
        s.connect(ai[0][-1])
        return s

    def canSend(self):
        """return true if interface can send data, false otherwise"""
        return self._wlan.isconnected()

    def send(self, data):
        """attempts to send via interface, returns success status"""
        #TODO encrypt data
        try:
            self._sock.write(data)
            return True
        except OSError:
            print("error!")
            self._sock.close()
            self.connect()
            self._sock = self.makeSock()
            return False
