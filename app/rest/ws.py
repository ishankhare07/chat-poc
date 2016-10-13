from tornado.websocket import WebSocketHandler
from .validators import PayloadValidator
from. validators.payload_validator import Result
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
        if result:
            pass
        else:
            """
                successful handshake
            """
            pass

    def on_close(self):
        # this needs more work for removing both connected and verified clients
        WsHandler.store.remove_verified(self.user_id, self)
