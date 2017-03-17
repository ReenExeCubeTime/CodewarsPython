class Mumbling(object):

    def accum(self, string):
        length = len(string)
        result = []
        for index in range(0, length):
            letter = string[index]
            result.append(letter.upper() + letter.lower() * index)
        return '-'.join(result)