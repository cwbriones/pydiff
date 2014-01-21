"""
Python implementation of diff.
"""
import sys

class Diff(object):
    """
    Solves the longest common subsequence problem for two strings to find
    their difference.
    """

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        
        self._table = self._compute_table(str1, str2)

    def _compute_table(self, str1, str2):
        """
        Computes the subsequence table.
        """
        table = [[0] * len(str2)] * len(str1)
        return table

    def lcs_length(self):
        """
        Returns the length of the longest common subsequence.
        """
        return self._table[-1][-1]

def main(argv):
    """
    Entry point.
    """
    pass

if __name__ == '__main__':
    main(sys.argv)
