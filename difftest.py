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

    def test_no_shared_suffix(self):
        self.diff = diff.Diff("abcd", "efgh")
        self.assertEqual("", self.diff._get_shared_suffix())

class SharedPrefixTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "thisisareallylongsuffix"
        self.str1 = self.prefix + "aaaaaaaa"
        self.str2 = self.prefix + "bbbbbbbb"
        self.diff = diff.Diff(self.str1, self.str2)

    def test_get_shared_prefix(self):
        self.assertEqual(self.diff._get_shared_prefix(), self.prefix)

    def test_no_shared_prefix(self):
        self.diff = diff.Diff("abcd", "efgh")
        self.assertEqual("", self.diff._get_shared_prefix())

class SharedPrefixSuffixTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
