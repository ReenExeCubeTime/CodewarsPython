class PersistentBugger(object):
    def persistence(self, n):
        while n > 10:
            digits = map(int, str(n).split(''))
            n = 1
            for digit in digits:
                n *= digit
        return n