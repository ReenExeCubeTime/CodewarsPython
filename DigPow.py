class DigPow(object):
    def calculate(self, n, p):
        digits = str(n)

        sum = 0
        for digitString in digits:
            digit = int(digitString)
            sum += digit ** p
            p += 1

        return sum / n if sum % n == 0 else -1