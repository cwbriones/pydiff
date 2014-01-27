"""
Python implementation of diff.
"""
import sys

class Diff(object):
    class Kind(object):
        ADD = 0
        SUB = 1
        NO_CHANGE = 2
        KINDS = 3
        ERROR = 4

    def __init__(self):
        self._diffs = []
        self._last_kind = Diff.Kind.ERROR
        self._current_line = []

    def add_char(self, kind, char):
        """
        Adds the char with Diff.Kind diff_kind to the Diff object.
        """
        if kind == self._last_kind:
            self._current_line.append(char)
        else:
            self.finish_line()
            self._current_line = [char]
        self._last_kind = kind

    def finish_line(self):
        """
        Adds the current line to the list of diff chunks if its type is valid.
        """
        if self._last_kind != Diff.Kind.ERROR:
            line = ''.join(self._current_line)
            self._diffs.append((self._last_kind, line))

    def print_out(self):
        """
        Prints out the diff.
        """
        print self._diffs
        leading_chars = { 
                Diff.Kind.ADD: '+', 
                Diff.Kind.SUB: '-', 
                Diff.Kind.NO_CHANGE: ' ' }
        for (kind, run) in self._diffs:
            char = leading_chars[kind]
            if run[-1] == '\n':
                run = run[:-1]
            if run[0] == '\n':
                run = run[1:]
            for line in run.split('\n'):
                print "{}{}".format(char, line)

class DiffTool(object):
    """
    Solves the longest common subsequence problem for two strings to find
    their difference.
    """

    def __init__(self, str1, str2):
        self._diff_object = None

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

    def get_diff(self):
        if self._diff_object is None:
            self._diff_object = Diff()
            self._build_diff(len(self.str1)-1, len(self.str2)-1)
            self._diff_object.finish_line()
        return self._diff_object

    def _build_diff(self, i, j):
        if i > 0 and j > 0 and self.str1[i] == self.str2[j]:
            self._build_diff(i-1, j-1)
            self._diff_object.add_char(Diff.Kind.NO_CHANGE, self.str1[i])
        elif j > 0 and (i == 0 or self._table[i][j-1] >= self._table[i-1][j]):
            self._build_diff(i, j-1)
            self._diff_object.add_char(Diff.Kind.ADD, self.str2[j])
        elif i > 0 and (j == 0 or self._table[i][j-1] < self._table[i-1][j]):
            self._build_diff(i-1, j)
            self._diff_object.add_char(Diff.Kind.SUB, self.str1[i])
        else:
            self._diff_object.add_char(Diff.Kind.SUB, self.str1[0])

def main(argv):
    """
    Entry point.
    """
    with open("one.txt") as file1:
        str1 = ''.join(file1.readlines())
    with open("two.txt") as file2:
        str2 = ''.join(file2.readlines())
    diff_tool = DiffTool(str1, str2)
    the_diff = diff_tool.get_diff()

    the_diff.print_out()

if __name__ == '__main__':
    main(sys.argv)
