import unittest

from SumTwoSmallestNumber import SumTwoSmallestNumber

class SumTwoSmallestNumberTest(unittest.TestCase):
    def test(self):
        summer = SumTwoSmallestNumber()
        self.assertEqual(summer.sum([5, 8, 12, 18, 22]), 13)
        self.assertEqual(summer.sum([7, 15, 12, 18, 22]), 19)
        self.assertEqual(summer.sum([25, 42, 12, 18, 22]), 30)

unittest.main()