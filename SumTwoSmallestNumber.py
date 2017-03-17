class SumTwoSmallestNumber(object):

    def sum(self, numbers):
        numbers.sort()

        return numbers[0] + numbers[1]