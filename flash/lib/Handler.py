class Handler:
    _commIfs = []

    def registerCommIf(commIf):
        """register a communications interface with the handler"""
        _commIfs.append(commIf)

    def send(data):
        """attempt to send data over first available interface"""
        for commIf in _commIfs:
            if commIf.canSend():
                if commIf.send(data):
                    return True
        return False
