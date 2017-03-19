import unittest

from VowelCount import VowelCount


class VowelCountTest(unittest.TestCase):
    def test(self):
        vowelCount = VowelCount()
        self.assertEqual(vowelCount.get_count("abracadabra"), 5)

unittest.main()