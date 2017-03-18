import unittest

from TriangularTreasure import TriangularTreasure

class TriangularTreasureTest(unittest.TestCase):
    def testPrime(self):
        triangular = TriangularTreasure()
        self.assertEqual(triangular.calculate(2), 3)
        self.assertEqual(triangular.calculate(4), 10)
        self.assertEqual(triangular.calculate(9), 45)
        self.assertEqual(triangular.calculate(-9), 0)


unittest.main()