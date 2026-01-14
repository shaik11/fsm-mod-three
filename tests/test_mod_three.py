import unittest
from fsm.mod_three import ModThreeFSM

class TestModThreeFSM(unittest.TestCase):

    def setUp(self):
        self.mod3 = ModThreeFSM()

    def test_cases(self):
        self.assertEqual(self.mod3.mod_three("0"), 0)
        self.assertEqual(self.mod3.mod_three("1"), 1)
        self.assertEqual(self.mod3.mod_three("10"), 2)
        self.assertEqual(self.mod3.mod_three("11"), 0)
        self.assertEqual(self.mod3.mod_three("110"), 0)
        self.assertEqual(self.mod3.mod_three("1010"), 1)
        self.assertEqual(self.mod3.mod_three("1101"), 1)
        self.assertEqual(self.mod3.mod_three("1110"), 2)
        self.assertEqual(self.mod3.mod_three("1111"), 0)        

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.mod3.mod_three("10201")

if __name__ == "__main__":
    unittest.main()