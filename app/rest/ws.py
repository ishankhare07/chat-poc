from .base import *
from tornado.websocket import WebSocketHandler
from .validators import *
import sys

class WsHandler(WebSocketHandler):
    connected = {}

    def open(self, user_id):
        # make it int until handshake validator not completed
        result = HandshakeValidator().load({'user_id': user_id})
        if result.errors:
            print('closing:', result)
            self.write_message(json.dumps(result.errors))
            self.close()
        else:
            WsHandler.connected[result.data['user_id']] = self
            self.user_id = result.data['user_id']
            self.write_message(json.dumps({
                "type": "handshake",
                "user_id": result.data['user_id']
            }))

    def on_message(self, message):
        result = MessageValidator().loads(message)

        if result.errors:
            print(result)
            self.write_message(json.dumps(result.errors))
        else:
            reply = result.data
            try:
                session.add(reply)
                session.commit()
            except:
                session.rollback()
                session.add(reply)
                session.commit()
            response = MessageValidator().dumps(reply).data

            # send reply to receipent
            try:
                WsHandler.connected[reply.to_user].write_message(response)
            except KeyError as ke:
                # receipent not yet connected
                print("Receipent {0} not connected".format(reply.to_user))
                print(WsHandler.connected)

    def on_close(self):
        try:
            WsHandler.connected.pop(self.user_id)
        except KeyError as ke:
            print('Client already removed or is not in connected')
