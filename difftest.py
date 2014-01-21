import diff
import unittest

class DiffIdenticalStringsTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_length_is_nonzero(self):
        test = diff.Diff("abcd", "abcd")
        self.assertGreater(test.lcs_length(), 0)

if __name__ == '__main__':
    unittest.main()
