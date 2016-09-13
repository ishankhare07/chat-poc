from .base import *
from tornado.websocket import WebSocketHandler

class WsHandler(WebSocketHandler):
    connected = []
    message_count = 0
    def open(self):
        WsHandler.connected.append(self)
        print("Connected clients >>", len(WsHandler.connected))
        self.write_message("connected")

    def on_message(self, message):
        for x in WsHandler.connected:
            x.write_message(message)
            WsHandler.message_count += 1
            reply = Reply(message=message,
                            enquiry_id=2,
                            from_user=2,
                            to_user=3)
            session.add(reply)
            session.commit()
            print("messages >>", WsHandler.message_count)

    def on_close(self):
        WsHandler.connected.remove(self)
