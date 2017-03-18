import unittest

from Default import Default


class DefaultTest(unittest.TestCase):
    def test(self):
        default = Default()
        self.assertEqual(default.calculate(1), 1)

unittest.main()