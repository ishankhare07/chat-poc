from ..rest.validators.handshake_validator import HandshakeValidator
import unittest


class HandshakeValidatorTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_user_id_valid(self):
        self.hs = HandshakeValidator()
        self.data = {
            "user_id"   : 1000,
            "jwt"       : "some jwt string"
                }
        self.assertEqual(self.hs.validate(self.data), {})

    def test_user_id_with_string(self):
        self.hs = HandshakeValidator()
        self.data = {
            "user_id"   : "spam",
            "jwt"       : "some jwt string"
                }
        self.assertNotEqual(self.hs.validate(self.data), {})


if __name__ == "__main__":
    unittest.main()
