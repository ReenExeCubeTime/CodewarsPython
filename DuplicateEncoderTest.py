import unittest

from DuplicateEncoder import DuplicateEncoder


class DuplicateEncoderTest(unittest.TestCase):
    def test(self):
        encoder = DuplicateEncoder()
        self.assertEqual(encoder.encode("din"), "(((")
        self.assertEqual(encoder.encode("recede"), "()()()")
        self.assertEqual(encoder.encode("Success"), ")())())", "should ignore case")
        self.assertEqual(encoder.encode("(( @"), "))((")

unittest.main()