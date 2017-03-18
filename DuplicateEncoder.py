from collections import defaultdict


class DuplicateEncoder(object):
    def encode(self, word):
        map = defaultdict(int)

        for char in word:
            map[char.lower()] += 1

        result = []
        for char in word:
            result.append(')' if map[char.lower()] > 1 else '(')

        return ''.join(result)
