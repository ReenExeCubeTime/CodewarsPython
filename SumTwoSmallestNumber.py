class SumTwoSmallestNumber(object):

    def sum(self, numbers):
        return sum(sorted(numbers)[:2])