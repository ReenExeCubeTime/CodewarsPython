import unittest

from HighestAndLowest import HighestAndLowest


class HighestAndLowestTest(unittest.TestCase):
    def test(self):
        highestAndLowest = HighestAndLowest()
        self.assertEqual(highestAndLowest.find("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
        self.assertEqual(highestAndLowest.find("1 -1"), "1 -1")
        self.assertEqual(highestAndLowest.find("1 1"), "1 1")
        self.assertEqual(highestAndLowest.find("-1 -1"), "-1 -1")
        self.assertEqual(highestAndLowest.find("1 -1 0"), "1 -1")
        self.assertEqual(highestAndLowest.find("1 1 0"), "1 0")
        self.assertEqual(highestAndLowest.find("-1 -1 0"), "0 -1")
        self.assertEqual(highestAndLowest.find("42"), "42 42")

unittest.main()