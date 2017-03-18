import string


class HighestAndLowest(object):
    def find(self, numbers):
        number_list = numbers.split(' ')

        first = int(number_list[0])
        max_number = first
        min_number = first

        for number in number_list:
            number = int(number)

            max_number = max(max_number, number)
            min_number = min(min_number, number)

        return str(max_number) + ' ' + str(min_number)
