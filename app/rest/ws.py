from .base import *
from tornado.websocket import WebSocketHandler
from .validators import *
import sys

class WsHandler(WebSocketHandler):
    connected = {}

    def open(self, user_id):
        # make it int until handshake validator not completed
        user_id = int(user_id)
        WsHandler.connected[user_id] = self
        self.user_id = user_id
        self.write_message(json.dumps({
            "type": "request",
            "request": "user_id",
            "user_id": user_id
            }))

    def on_message(self, message):
        print(type(message), message)
        data = json.loads(message)

        result = MessageValidator().loads(message)

        if result.errors:
            print(result)
            self.write_message(json.dumps(result.errors))
        else:
            reply = result.data
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
        WsHandler.connected.pop(self.user_id)
