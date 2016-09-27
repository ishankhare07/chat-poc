from .base import *
from tornado.websocket import WebSocketHandler
from .validators import PayloadValidator
from .validators import HandshakeValidator
from .global_store import GlobalStore

class WsHandler(WebSocketHandler):
    store = GlobalStore()

    def open(self, user_id):
        # make it int until handshake validator not completed
        result = HandshakeValidator().load({'user_id': user_id})
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
        result = PayloadValidator().validate(message, self)

        if result.errors:
            print(result)
            self.write_message(json.dumps(result.errors))
        else:
            reply = result.data
            session.add(reply)
            session.commit()
            response = PayloadValidator().unmarshal(result.data)
            try:
                session.add(reply)
                session.commit()
            except:
                session.rollback()
                session.add(reply)
                session.commit()
            response = PayloadValidator().unmarshal(reply)

            # send reply to receipent
            for connection in WsHandler.store.connected.get(reply.to_user, []):
                connection.write_message(response)
            if not connection:
                # receipent not yet connected
                print("Receipent {0} not connected".format(reply.to_user))
                print(WsHandler.store.connected)

    def on_close(self):
        try:
            # this needs more work for removing both connected and verified clients
            WsHandler.store.remove_connected(self.user_id, self)
            print(WsHandler.store.connected)
        except KeyError as ke:
            print('Client already removed or is not in connected')
