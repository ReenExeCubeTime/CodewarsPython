import math


class Prime(object):

    def backwards(self, start, stop):
        to = stop + 1
        map = list(range(0, to))

        max = math.floor(math.sqrt(stop)) + 1

        delimiter = 2

        while delimiter < max:
            complex = delimiter

            while complex < to:
                map[complex] = 0
                complex += delimiter

            delimiter += 1

        slice = map[start:to]

        primes = set(slice) - set([0])

        backwards = []
        for prime in primes:
            reverse = int(str(prime)[::-1])
            if reverse < to and map[reverse]:
                backwards.append(prime)

        backwards.sort()
        return backwards


