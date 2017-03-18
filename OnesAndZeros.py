class OnesAndZeros(object):
    def array_to_number(self, arr):
        sum = 0
        for bit in arr:
            sum = (sum << 1) | bit
        return sum