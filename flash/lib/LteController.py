class LteController:
    def canSend(self):
        """return true if interface can send data, false otherwise"""
        return False

    def send(self, data):
        """attempts to send via interface, returns success status"""
        return False
