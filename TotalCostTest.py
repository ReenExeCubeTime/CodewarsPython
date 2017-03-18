import unittest

from TotalCost import TotalCost

class TotalCostTest(unittest.TestCase):
    def test(self):
        cost = TotalCost()
        costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
        self.assertEqual(cost.calculate(costs, ['socks', 'shoes'], 0.09), 70.85)
        self.assertEqual(cost.calculate(costs, ['shirt', 'shoes'], 0.05), 63.00)

unittest.main()