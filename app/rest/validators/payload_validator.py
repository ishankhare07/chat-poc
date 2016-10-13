from .handshake_validator import HandshakeValidator
from .message_validator import MessageValidator
from .acknowledgement_validator import AcknowledgementValidator
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
        except:
            websocket.write_message(json.dumps(
                errors={
                "type": "error",
                "message": "invalid json"
                }))

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
            response = PayloadValidator.unmarshal(result.data)

            # send acks
            ack = PayloadValidator.parse_reply_to_ack(response)
            for connection in PayloadValidator.store.verified.get(result.data.from_user, []):
                connection.write_message(ack)

            # send reply to receipent
            connection = None
            for connection in PayloadValidator.store.verified.get(result.data.to_user, []):
                connection.write_message(PayloadValidator.unmarshal(result.data))
            if not connection:
                # receipent not yet connected
                print("Receipent {0} not connected".format(result.data.to_user))
                print(PayloadValidator.store.connected)


            return result

        elif data['type'] == 'handshake':
            # use HandshakeValidator
            result = HandshakeValidator().load(data)
            result.data['type'] = 'handshake'
            if not result.errors:
                # no errors hence move from connected to verified
                PayloadValidator.store.move_to_verified(result.data['user_id'], websocket)

            # fetch un-received messages for this client
            for message in session.query(Reply).filter_by(to_user=result.data['user_id'],
                                                            received=False).all():
                print(message)
                websocket.write_message(
                            PayloadValidator.unmarshal(message))
            return

        elif data['type'] == 'acknowledgement':
            result = AcknowledgementValidator().load(data)
            for connection in PayloadValidator.store.verified.get(result.data['to_user'], []):
                connection.write_message(json.dumps(result.data))

    @staticmethod
    def unmarshal(data):
        if data.type == 'message':
            return MessageValidator().dumps(data).data
        elif data.type == 'acknowledgement':
            return AcknowledgementValidator().dumps(data).data

    @staticmethod
    def parse_reply_to_ack(response):
        reply = json.loads(response)
        reply['type'] = 'acknowledgement'
        reply['category'] = 'server-received'
        return AcknowledgementValidator().dump(reply).data
