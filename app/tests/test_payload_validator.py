from ..rest.validators.payload_validator import PayloadValidator, session
from ..rest.validators.models.replies import Reply
import unittest
import json

class PayloadValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self.pv = PayloadValidator()
        self.message_payload = json.dumps({
            "type": "message",
            "enquiry_id": 779,
            "from_user": 2561,
            "to_user": 2562,
            "message": "spam",
            "local_msg_id": 1234
            })

        self.handshake_payload = json.dumps({
            "type": "handshake",
            "user_id": 1234,
            "jwt": "some jwt as a string"
            })

        self.acknowledgement_payload = {
            "type": "acknowledgement",
            "id": 12345,
            "category": 'server-received'
            }

        self.invalid_json = [1,2,3,4,5]

        self.reply_data = {
            "enquiry_id": 779,
            "from_user": 2561,
            "to_user": 2562,
            "message": "spam",
            "local_msg_id": 12345
                }


    def test_incomplete_handshake(self):
        self.assertIsNotNone(self.pv.validate(self.message_payload).errors)

    def test_handshake_payload(self):
        self.assertFalse(self.pv.validate(self.handshake_payload).errors)

    def test_invalid_json(self):
        self.assertIsNotNone(self.pv.validate(self.invalid_json).errors)

    def test_message_payload(self):
        self.pv.store.verified[2561] = 'one'
        self.assertFalse(self.pv.validate(self.message_payload, websocket='one').errors)

    def test_unmarshalling(self):
        self.pv.store.verified[2561] = 'one'
        result = self.pv.validate(self.message_payload, websocket='one')
        unmarshalled = self.pv.unmarshal(result.data)
        marshalled = json.loads(unmarshalled)
        del marshalled['id']
        self.assertEqual(
                marshalled,
                json.loads(self.message_payload)
                )

    def test_acknowledgement_payload(self):
        reply = Reply(**self.reply_data)
        session.add(reply)
        session.commit()

        self.acknowledgement_payload['id'] = reply.id
        self.assertFalse(self.pv.validate(json.dumps(self.acknowledgement_payload)).errors)

    def tearDown(self):
        session.query(Reply).filter_by(from_user=2561, to_user=2562, enquiry_id=779).delete()
        session.commit()
