from tornado.websocket import WebSocketHandler
from .validators import PayloadValidator
from .validators import EndpointValidator
from .global_store import GlobalStore
from logentries import LogentriesHandler
from .validators.base import session
import logging
import json

class WsHandler(WebSocketHandler):
    store = GlobalStore()
    log = logging.getLogger('logentries')
    log.setLevel(logging.INFO)
    log.addHandler(LogentriesHandler('58ba03d6-2305-42bd-b0e7-af3ccfd1b698'))

    def check_origin(self, origin):
        return True

    def open(self, user_id):
        # make it int until handshake validator not completed
        result = EndpointValidator().load({'user_id': user_id})
        if result.errors:
            print('closing:', result)
            WsHandler.log.info('closing:', result)
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
        try:
            result = PayloadValidator.validate(message, self)
        except Exception as e:
            session.rollback()
            WsHandler.log.exception(e)
            return
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
