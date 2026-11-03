import unittest
from slot_machine import slot_machine

class SlotMachineTest(unittest.TestCase):
    def test_deux_premiers_identiques(self):
        self.assertEqual(slot_machine(5, ['+', '+', '%']), 10)

    def test_aucun_motif(self):
        self.assertEqual(slot_machine(5, ['+', '%', '+']), 0)

if __name__ == "__main__":
    unittest.main()
