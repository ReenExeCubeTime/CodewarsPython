class PersistentBugger(object):
    def persistence(self, n):
        if n < 10:
            return 0

        while n > 9:
            digits = str(n)
            n = 1
            for digit in digits:
                n *= int(digit)
        return n