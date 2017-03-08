import unittest

from Prime import Prime

class DefaultTest(unittest.TestCase):
    def testPrime(self):
        prime = Prime()
        self.assertEqual(prime.fromRange(9000, 10000), None)
        self.assertEqual([9923, 9931, 9941, 9967], [9923, 9931, 9941, 9967])


unittest.main()