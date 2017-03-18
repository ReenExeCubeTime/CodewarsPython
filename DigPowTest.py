import unittest

from DigPow import DigPow

class DigPowTest(unittest.TestCase):
    def test(self):
        digPow = DigPow()
        self.assertEqual(digPow.calculate(89, 1), 1)
        self.assertEqual(digPow.calculate(92, 1), -1)
        self.assertEqual(digPow.calculate(46288, 3), 51)

unittest.main()