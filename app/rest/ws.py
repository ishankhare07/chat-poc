from tornado.websocket import WebSocketHandler
from .validators import PayloadValidator
from .validators import EndpointValidator
from .global_store import GlobalStore
import json

class WsHandler(WebSocketHandler):
    store = GlobalStore()

    def open(self, user_id):
        # make it int until handshake validator not completed
        result = EndpointValidator().load({'user_id': user_id})
        if result.errors:
            print('closing:', result)
            self.write_message(json.dumps(result.errors))
            self.close()
        else:
            WsHandler.store.connected[result.data['user_id']] = self
            self.user_id = result.data['user_id']
            self.write_message(json.dumps({
                "type": "handshake",
                "user_id": result.data['user_id']
            }))

    def on_message(self, message):
        result = PayloadValidator.validate(message, self)

        if result.errors:
            self.write_message(json.dumps(result.errors))
        elif result.data:
            reply = result.data

            # send server-received acknowledgement to sender
            ack = PayloadValidator.parse_reply_to_ack(reply)
            for connection in WsHandler.store.verified.get(reply.from_user, []):
                connection.write_message(ack)

            
            # get responses
            response = PayloadValidator().unmarshal(reply)

            # send reply to receipent
            connection = None
            for connection in WsHandler.store.verified.get(reply.to_user, []):
                connection.write_message(response)
            if not connection:
                # receipent not yet connected
                print("Receipent {0} not connected".format(reply.to_user))
                print(WsHandler.store.connected)

        else:
            """
                successful handshake
            """
            pass

    def on_close(self):
        # this needs more work for removing both connected and verified clients
        WsHandler.store.remove_verified(self.user_id, self)
