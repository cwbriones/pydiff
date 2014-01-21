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
        for (i, char1) in enumerate(str1):
            for (j, char2) in enumerate(str2):
                if char1 == char2:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])

        return table

    def lcs_length(self):
        """
        Returns the length of the longest common subsequence.
        """
        return self._table[-1][-1]

    def lcs(self):
        """
        Returns the longest common subsequence (or the first one it finds)
        """
        return self._backtrack(len(self.str1)-1, len(self.str2)-1)

    def _backtrack(self, i, j):
        """
        Backtracks to build the LCS from the table computed.
        """
        if i == 0 or j == 0:
            if self.str1[i] == self.str2[j]:
                return self.str1[i]
            else:
                return ""
        elif self.str1[i] == self.str2[j]:
            return self._backtrack(i-1, j-1) + self.str1[i]
        else:
            if self._table[i][j-1] > self._table[i-1][j]:
                return self._backtrack(i, j-1)
            else:
                return self._backtrack(i-1, j)

def main(argv):
    """
    Entry point.
    """
    pass

if __name__ == '__main__':
    main(sys.argv)
