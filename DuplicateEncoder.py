class DuplicateEncoder(object):
    def encode(self, word):
        lower = word.lower()
        return "".join(["(" if lower.count(char) == 1 else ")" for char in lower])
