# Regex matching algorithms
# You will be given a string and a pattern string consisting of only '*','?', and small letters. You have to return tree or false based upon the comparisons.
# ? repersent one char.
# * means zero or n number of char for any positive n.
#
# Example
# abc, a?c : true
# abc, a*?c : true
# abc, * : true
# abc, ?c : false

import unittest


def regex_match(st, reg):
    i = 0
    j = 0
    reg_len = len(reg)
    while i < len(st) and j < reg_len:
        if reg[j].isalpha():
            if st[i] != reg[j]:
                return False
            i = i + 1
            j = j + 1
        elif reg[j] == '?':
            i = i + 1
            j = j + 1
        elif reg[j] == '*':
            if j == reg_len - 1:
                i = i + 1
            else:
                j = j + 1
    return True


class Test(unittest.TestCase):
    in_out = [['abc', 'a?c', True], ['abc', 'a*?c', True], ['abc', '*', True], ['abc', '?c', False], ['abc', 'a*', True]]

    def test_regex_match(self):
        for st, reg, out in self.in_out:
            output = regex_match(st, reg)
            self.assertEqual(output, out)

if __name__ == '__main__':
    unittest.main()
