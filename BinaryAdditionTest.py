import unittest

from BinaryAddition import BinaryAddition


class BinaryAdditionTest(unittest.TestCase):
    def test(self):
        addition = BinaryAddition()
        self.assertEqual(addition.add(1, 1), "10")
        self.assertEqual(addition.add(0, 1), "1")
        self.assertEqual(addition.add(1, 0), "1")
        self.assertEqual(addition.add(2, 2), "100")
        self.assertEqual(addition.add(51, 12), "111111")

unittest.main()