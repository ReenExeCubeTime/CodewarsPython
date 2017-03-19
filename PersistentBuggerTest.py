import unittest

from PersistentBugger import PersistentBugger


class PersistentBuggerTest(unittest.TestCase):
    def test(self):
        bugger = PersistentBugger()
        self.assertEqual(bugger.persistence(39), 3)
        self.assertEqual(bugger.persistence(4), 0)
        self.assertEqual(bugger.persistence(25), 2)
        self.assertEqual(bugger.persistence(999), 4)

unittest.main()