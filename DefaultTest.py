import unittest


class DefaultTest(unittest.TestCase):
    def test(self):
        self.assertEqual([9923, 9931, 9941, 9967], [9923, 9931, 9941, 9967])


unittest.main()