import unittest

from HumanReadableTime import HumanReadableTime


class HumanReadableTimeTest(unittest.TestCase):
    def test(self):
        humanReadableTime = HumanReadableTime()
        self.assertEqual(humanReadableTime.make(0), "00:00:00")
        self.assertEqual(humanReadableTime.make(5), "00:00:05")
        self.assertEqual(humanReadableTime.make(60), "00:01:00")
        self.assertEqual(humanReadableTime.make(86399), "23:59:59")
        self.assertEqual(humanReadableTime.make(359999), "99:59:59")

unittest.main()