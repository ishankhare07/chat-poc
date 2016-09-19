from .base import *
from tornado.websocket import WebSocketHandler
from .validators import *
import sys

class WsHandler(WebSocketHandler):
    connected = {}

    def open(self, user_id):
        WsHandler.connected[user_id] = self
        self.user_id = user_id
        self.write_message(json.dumps({
            "type": "request",
            "request": "user_id",
            "user_id": user_id
            }))

    def on_message(self, message):
        data = json.loads(message)

        result = MessageValidator().load(data)

        if result.errors:
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
                print("Receipent not connected")

    def on_close(self):
        WsHandler.connected.pop(self.user_id)
