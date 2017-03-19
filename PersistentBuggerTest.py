import unittest

from PersistentBugger import PersistentBugger


class PersistentBuggerTest(unittest.TestCase):
    def test(self):
        bugger = PersistentBugger()
        self.assertEqual(bugger.persistence(39), 4)
        self.assertEqual(bugger.persistence(4), 0)
        self.assertEqual(bugger.persistence(999), 2)

unittest.main()