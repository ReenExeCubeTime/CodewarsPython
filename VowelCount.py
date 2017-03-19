class VowelCount(object):
    def get_count(self, inputStr):
        VOWELS = "aeiou"
        count = 0
        for vowel in VOWELS:
            count += inputStr.count(vowel)
        return count