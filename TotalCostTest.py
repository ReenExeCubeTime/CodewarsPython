import unittest

from TotalCost import TotalCost

class TotalCostTest(unittest.TestCase):
    def testPrime(self):
        cost = TotalCost()
        costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
        self.assertEqual(cost.calculate(costs, ['socks', 'shoes'], 0.09), 70.85)

unittest.main()