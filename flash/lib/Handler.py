import logging

class Handler:
    _commIfs = []
    logger = None

    def __init__():
        logger = logging.getLogger("logger")

    def registerCommIf(commIf):
        """register a communications interface with the handler"""
        _commIfs.append(commIf)

    def send(data):
        """attempt to send data over first available interface"""
        for commIf in _commIfs:
            if commIf.canSend():
                logger.debug( commIf.name() "can send")
                if commIf.send(data):
                    logger.debug( commIf.name() "sent")
                    return True
                logger.debug( commIf.name() "failed to send")
            logger.debug( commIf.name() "can't send")
        logger.warning("No commIf can send at this time")
        return False
