class FirstUniqueLetter(object):
    def find(self, string):
        lower = string.lower()
        for i, letter in enumerate(lower):
            if lower.count(letter) == 1:
                return string[i]
        return ''