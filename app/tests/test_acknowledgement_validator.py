from ..rest.validators.acknowledgement_validator import AcknowledgementValidator, session
from ..rest.validators.models.existing_models import Reply
import unittest
import json

class AcknowledgementValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self.ack_v = AcknowledgementValidator()
        self.data = {
            "type": "acknowledgement",
            "id": 12345,
            "category": 'server-received'
            }

        self.reply_data = {
            "enquiry_id": 779,
            "from_user": 2561,
            "to_user": 2562,
            "message": "spam",
            "local_msg_id": 12345
                }


    def test_ack_validation(self):
        self.assertFalse(self.ack_v.validate(self.data))

    def test_invalid_type(self):
        self.data['type'] = 'spam'
        self.assertTrue(self.ack_v.validate(self.data))

    def test_negative_message_id(self):
        self.data['id'] = -1
        self.assertTrue(self.ack_v.validate(self.data))

    def test_result_object(self):
        reply = Reply(**self.reply_data)
        session.add(reply)
        session.commit()

        self.data['id'] = reply.id
        self.assertIsInstance(self.ack_v.load(self.data).data, Reply)

    def test_unmarshalling(self):
        reply = Reply(**self.reply_data)
        session.add(reply)
        session.commit()

        self.data['id'] = reply.id
        result = self.ack_v.load(self.data)
        self.assertIsNotNone(self.ack_v.dumps(result.data).data)

    def tearDown(self):
        session.query(Reply).filter_by(from_user=self.reply_data['from_user'],
                                    to_user=self.reply_data['to_user'],
                                    enquiry_id=779).delete()
