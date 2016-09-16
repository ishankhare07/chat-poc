from .base import *
from tornado.websocket import WebSocketHandler
from .parsers import *

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

        result = MessageParser().load(data)

        if result.errors:
            self.write_message(json.dumps(result.errors))
        else:
            reply = result.data
            session.add(reply)
            session.commit()
            #pprint(result.data, indent=2)
            #pprint(result.errors, indent=2)
            response = MessageParser().dumps(reply).data
            
            # send reply to receipent
            try:
                WsHandler.connected[reply.to_user].write_message(response)
            except KeyError as ke:
                print(ke)

        '''
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
        '''

    def on_close(self):
        WsHandler.connected.pop(self.user_id)
