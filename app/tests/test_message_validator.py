from ..rest.validators.message_validator import MessageValidator
from ..rest.validators.models.replies import Reply
import unittest
import json
import copy

class MessageValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self.mv = MessageValidator()
        self.data = {
            "type": "message",
            "enquiry_id": 2354,
            "from_user": 12,
            "to_user": 13,
            "message": "some message",
            "local_msg_id": 234
            }

    def test_message_loading(self):
        self.assertEqual(self.mv.validate(self.data), {})

    def test_message_type(self):
        data = copy.deepcopy(self.data)
        data['type'] = 'spam'
        self.assertNotEqual(self.mv.validate(data), {})

    def test_negative_local_msg_id(self):
        data = copy.deepcopy(self.data)
        data['local_msg_id'] = -1
        self.assertNotEqual(self.mv.validate(data), {})

    def test_reply_object(self):
        self.assertTrue(isinstance(self.mv.load(self.data).data, Reply))
