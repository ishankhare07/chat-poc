from .test_handshake_validator import HandshakeValidatorTestCase
from .test_message_validator import MessageValidatorTestCase
from .test_payload_validator import PayloadValidatorTestCase
from .test_global_store import GlobalStoreTestCase, ModifiedDictTestCase
from .test_acknowledgement_validator import AcknowledgementValidatorTestCase
import unittest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(HandshakeValidatorTestCase))
suite.addTest(unittest.makeSuite(MessageValidatorTestCase))
suite.addTest(unittest.makeSuite(PayloadValidatorTestCase))
suite.addTests([unittest.makeSuite(GlobalStoreTestCase),
            unittest.makeSuite(ModifiedDictTestCase)
            ]),
suite.addTest(unittest.makeSuite(AcknowledgementValidatorTestCase))

runner = unittest.TextTestRunner(verbosity=2)
