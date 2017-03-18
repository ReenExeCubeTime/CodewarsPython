import string


class ReplaceAlphabetPosition(object):

    def replace(self, text):
        result = []
        letters = string.ascii_uppercase
        shift = ord("A") - 1
        for letter in text:
            letter = letter.upper()
            if letter in letters:
                result.append(str(ord(letter) - shift))

        return " ".join(result)