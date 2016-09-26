from .handshake_validator import HandshakeValidator
from .message_validator import MessageValidator
from json.decoder import JSONDecodeError
import json

class Result:
    """
        This class will only be used in case of a JSON decode error
        when the message sent is not in properly formatted JSON
    """


    def __init__(self, data={}, errors={}):
        self.data = data
        self.errors = errors

class PayloadValidator:
    """
        Used as a filter to delegate different validators for different
        types of messages
    """


    @staticmethod
    def validate(payload):
        try:
            data = json.loads(payload)
        except JSONDecodeError as decodeError:
            return Result(errors={
                "type": "error",
                "message": "invalid json"
                })

        if data['type'] == 'message':
            # use MessageValidator
            result = MessageValidator().load(data)
            result.data.type = 'message'
            return result
        elif data['type'] == 'handshake':
            # use HandshakeValidator
            result = HandshakeValidator().load(data)
            result.data.type = 'handshake'
            return result

    @staticmethod
    def unmarshal(data):
        if data.type == 'message':
            return MessageValidator().dumps(data).data
        elif data.type == 'handshake':
            return HandshakeValidator().dumps(data).data

