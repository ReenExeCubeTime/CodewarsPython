class TotalCost(object):

    def calculate(self, costs, items, tax):
        sum = 0
        for item in items:
            if item in costs:
                sum += costs[item]
        return sum + sum * tax