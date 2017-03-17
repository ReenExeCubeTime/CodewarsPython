import unittest

from Prime import Prime

class PrimeTest(unittest.TestCase):
    def testPrime(self):
        prime = Prime()
        self.assertEqual(prime.backwards(9900, 10000), [9923, 9931, 9941, 9967])
        self.assertEqual(prime.backwards(7000, 7060), [7027, 7043, 7057])


unittest.main()