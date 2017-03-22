import unittest

from FirstUniqueLetter import FirstUniqueLetter


class FirstUniqueLetterTest(unittest.TestCase):
    def test(self):
        finder = FirstUniqueLetter()
        self.assertEqual(finder.find('a'), 'a')
        self.assertEqual(finder.find('stress'), 't')
        self.assertEqual(finder.find('moonmen'), 'e')

        self.assertEqual(finder.find(''), '')

        self.assertEqual(finder.find('abba'), '')
        self.assertEqual(finder.find('aa'), '')

        self.assertEqual(finder.find('~><#~><'), '#')
        self.assertEqual(finder.find('hello world, eh?'), 'w')

        self.assertEqual(finder.find('sTreSS'), 'T')
        self.assertEqual(finder.find('Go hang a salami, I\'m a lasagna hog!'), ',')

unittest.main()