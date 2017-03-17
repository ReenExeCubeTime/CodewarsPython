class TotalCost(object):

    def calculate(self, costs, items, tax):
        sum = 0
        for item in items:
            sum += costs[item]
        return sum + sum * tax