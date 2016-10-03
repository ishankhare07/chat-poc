from .handshake_validator import HandshakeValidator
from .message_validator import MessageValidator
from ..global_store import GlobalStore
from json.decoder import JSONDecodeError
from .base import *
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

    store = GlobalStore()

    @staticmethod
    def validate(payload, websocket=None):
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

            if websocket not in PayloadValidator.store.verified[result.data.from_user]:
                return Result(errors={
                    "type": "error",
                    "message": "Handshake not completed"
                    })
            try:
                session.add(result.data)
                session.commit()
            except:
                session.rollback()
                session.add(result.data)
                session.commit()

            result.data.type = 'message'
            return result

        elif data['type'] == 'handshake':
            # use HandshakeValidator
            result = HandshakeValidator().load(data)
            result.data['type'] = 'handshake'
            if not result.errors:
                # no errors hence move from connected to verified
                PayloadValidator.store.move_to_verified(result.data['user_id'], websocket)
            return Result(data=None)

    @staticmethod
    def unmarshal(data):
        if data.type == 'message':
            return MessageValidator().dumps(data).data
        elif data['type'] == 'handshake':
            return HandshakeValidator().dumps(data).data

