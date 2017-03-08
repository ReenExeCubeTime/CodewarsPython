import math


class Prime(object):

    def backwards(self, start, stop):
        to = stop + 1
        maxBack = max(10000, to)
        map = list(range(0, maxBack))

        maxDelimiter = math.floor(math.sqrt(stop)) + 1

        delimiter = 2

        while delimiter < maxDelimiter:
            complex = delimiter

            while complex < maxBack:
                map[complex] = 0
                complex += delimiter

            delimiter += 1

        slice = map[start:to]

        primes = set(slice) - set([0])

        backwards = []
        for prime in primes:
            reverse = int(str(prime)[::-1])
            if map[reverse] > 0:
                backwards.append(prime)

        backwards.sort()
        return backwards


