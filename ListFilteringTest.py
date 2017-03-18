import unittest

from ListFiltering import ListFiltering

class ListFilteringTest(unittest.TestCase):
    def test(self):
        listFiltering = ListFiltering()
        self.assertEqual(listFiltering.filter([1, 2, 'a', 'b']), [1, 2])
        self.assertEqual(listFiltering.filter([1, 'a', 'b', 0, 15]), [1, 0, 15])
        self.assertEqual(listFiltering.filter([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123])

unittest.main()