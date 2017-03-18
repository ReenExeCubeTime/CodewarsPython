class ListFiltering(object):
    def filter(self, l):
        result = []
        for item in l:
            if type(item) is int:
                result.append(item)

        return  result