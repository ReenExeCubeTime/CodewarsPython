import unittest

from OnesAndZeros import OnesAndZeros


class OnesAndZerosTest(unittest.TestCase):
    def test(self):
        onesAndZeros = OnesAndZeros()
        self.assertEqual(onesAndZeros.array_to_number([0, 0, 0, 1]), 1)
        self.assertEqual(onesAndZeros.array_to_number([0, 0, 1, 0]), 2)
        self.assertEqual(onesAndZeros.array_to_number([1, 1, 1, 1]), 15)
        self.assertEqual(onesAndZeros.array_to_number([0, 1, 1, 0]), 6)

unittest.main()