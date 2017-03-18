class ListFiltering(object):
    def filter(self, l):
        return [i for i in l if isinstance(i, int)]