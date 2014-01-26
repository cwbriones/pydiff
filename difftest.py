import diff
import unittest

class DiffIdenticalStringsTest(unittest.TestCase):

    def setUp(self):
        self.str = "abcd"
        self.diff = diff.Diff(self.str, self.str)

    def test_length_is_nonzero(self):
        self.assertGreater(self.diff.lcs_length(), 0)

    def test_lcs_is_the_whole_thing(self):
        self.assertEqual(self.diff.lcs_length(), len(self.str))
        self.assertEqual(self.diff.lcs(), self.str)

class SharedSuffixTest(unittest.TestCase):

    def setUp(self):
        self.suffix = "thisisareallylongsuffix"
        self.str1 = "aaaaaaaa" + self.suffix
        self.str2 = "bbbbbbbb" + self.suffix
        self.diff = diff.Diff(self.str1, self.str2)

    def test_get_shared_suffix(self):
        self.assertEqual(self.diff._get_shared_suffix(), self.suffix)

class SharedPrefixTest(unittest.TestCase):
    pass

class SharedPrefixSuffixTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
