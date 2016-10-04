from ..rest.global_store import *
import unittest

class GlobalStoreTestCase(unittest.TestCase):
    def test_connected_property(self):
        self.assertIsInstance(GlobalStore().connected, ModifiedDict)

    def test_remove_connected(self):
        gs = GlobalStore()
        gs.connected[1] = 'one'
        gs.connected[1] = 'two'
        self.assertTrue(gs.remove_connected(1, 'one'))
        self.assertTrue(gs.remove_connected(1, 'two'))
        self.assertFalse(gs.remove_connected(1, 'one'))

    def test_remove_verified(self):
        gs = GlobalStore()
        gs.verified[1] = 'one'
        gs.verified[1] = 'two'
        gs.remove_verified(1, 'one')
        gs.remove_verified(1, 'two')
        self.assertFalse(gs.verified[1])

    def test_move_to_verified(self):
        gs = GlobalStore()
        gs.connected[1] = 'one'
        gs.connected[1] = 'two'
        gs.move_to_verified(1, 'one')
        self.assertEqual(gs.connected[1], ['two'])
        self.assertIsNotNone(gs.verified[1])

    def tearDown(self):
        gs = GlobalStore()
        gs.connected.clear()
        gs.verified.clear()


class ModifiedDictTestCase(unittest.TestCase):
    def test_get(self):
        md = ModifiedDict()
        md[1] = 'one'
        self.assertIsNotNone(md.get(1))

    def test_repr(self):
        md = ModifiedDict()
        md[1] = 'one'
        self.assertTrue(str(md))
