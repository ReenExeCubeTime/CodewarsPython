class HumanReadableTime(object):
    def __pad(self, number):
        return str(number) if number > 9 else "0" + str(number)
    def make(self, seconds):
        s = seconds % 60
        minutes = seconds // 60
        m = minutes % 60
        h = min(minutes // 60, 99)
        return ":".join(map(self.__pad, [h, m, s]))