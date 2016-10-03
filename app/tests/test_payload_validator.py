from ..rest.validators.payload_validator import PayloadValidator
import unittest
import json

class PayloadValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self.pv = PayloadValidator()
        self.message_payload = json.dumps({
            "type": "message",
            "enquiry_id": 1234,
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

    def test_message_payload(self):
        self.assertEqual(self.pv.validate(self.message_payload).errors, {})

    def test_handshake_payload(self):
        self.assertEqual(self.pv.validate(self.handshake_payload).errors, {})
