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

        self._prefix = self._get_shared_prefix()
        self._trim_prefix()
        self._suffix = self._get_shared_suffix()
        self._trim_suffix()

        self._table = self._compute_table(self.str1, self.str2)

    def _get_shared_prefix(self):
        """
        Returns the longest continuous substring shared by
        both strings starting from the front.
        """
        prefix = []
        for (char1, char2) in zip(self.str1, self.str2):
            if char1 != char2:
                break
            prefix.append(char1)
        return "".join(prefix)

    def _get_shared_suffix(self):
        """
        Returns the longest continuous substring shared by
        both strings ending at the back.
        """
        suffix = []
        for (char1, char2) in zip(reversed(self.str1), reversed(self.str2)):
            if char1 != char2:
                break
            suffix.insert(0, char1)
        return "".join(suffix)

    def _trim_prefix(self):
        """
        Removes the shared prefix and suffix from the input strings.
        """
        start = len(self._prefix)

        self.str1 = self.str1[start:]
        self.str2 = self.str2[start:]

    def _trim_suffix(self):
        """
        Removes the shared suffix from the input strings.
        """
        end = len(self._suffix) * -1

        if end != 0:
            self.str1 = self.str1[:end]
            self.str2 = self.str2[:end]

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
        length = len(self._prefix) + len(self._suffix)
        if (self.str1 != '' and self.str2 != ''):
            length += self._table[-1][-1]
        return length

    def lcs(self):
        """
        Returns the longest common subsequence (or the first one it finds)
        """
        if (self.str1 != '' and self.str2 != ''):
            lcs = self._backtrack(len(self.str1)-1, len(self.str2)-1)
        else:
            lcs = ''
        return self._prefix + lcs + self._suffix

    def _backtrack(self, i, j, chars=[]):
        """
        Backtracks to build the LCS from the table computed.
        """
        if i == 0 or j == 0:
            if self.str1[0] == self.str2[0]:
                chars.insert(0, self.str1[0])
            return ''.join(chars)
        elif self.str1[i] == self.str2[j]:
            chars.insert(0, self.str1[i])
            return self._backtrack(i-1, j-1, chars)
        else:
            if self._table[i][j-1] > self._table[i-1][j]:
                return self._backtrack(i, j-1, chars)
            else:
                return self._backtrack(i-1, j, chars)

def main(argv):
    """
    Entry point.
    """
    pass

if __name__ == '__main__':
    main(sys.argv)
