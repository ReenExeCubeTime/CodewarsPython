class ReplaceAlphabetPosition(object):

    def replace(self, text):
        result = []
        shift = ord("A") - 1
        for letter in text :
            if letter.isalpha():
                result.append(str(ord(letter.upper()) - shift))

        return " ".join(result)