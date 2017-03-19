class HumanReadableTime(object):
    def make(self, seconds):
        s = seconds % 60
        minutes = seconds // 60
        m = minutes % 60
        h = minutes // 60
        return '{:02}:{:02}:{:02}'.format(h, m, s)