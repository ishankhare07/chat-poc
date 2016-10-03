from .test_handshake_validator import HandshakeValidatorTestCase
from .test_message_validator import MessageValidatorTestCase
from .test_payload_validator import PayloadValidatorTestCase
import unittest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(HandshakeValidatorTestCase))
suite.addTest(unittest.makeSuite(MessageValidatorTestCase))
suite.addTest(unittest.makeSuite(PayloadValidatorTestCase))

runner = unittest.TextTestRunner(verbosity=2)
