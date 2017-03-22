class FirstUniqueLetter(object):
    def find(self, string):
        lower = string.lower()
        for letter in lower:
            if lower.count(letter) == 1:
                index = lower.find(letter)
                return string[index]
        return ''