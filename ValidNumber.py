"""
65. Valid Number
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
"""
# O(n)
# O(1)
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        flag_num, flag_dot, flag_e = False, False, False
        if not s:
            return False
        if s[0] not in "0123456789+-.":
            return False
        if s[0].isdigit():
            flag_num = True
        elif s[0] == ".":
            flag_dot = True
        i = 1
        while i < len(s):
            if s[i] in "eE":
                if not flag_num or flag_e:
                    return False
                flag_e, flag_dot, flag_num = True, True, False
                if i + 1 < len(s) and s[i + 1] in "+-":
                    i += 1
            elif s[i] == ".":
                if flag_dot:
                    return False
                flag_dot = True
            elif s[i].isdigit():
                flag_num = True
            else:
                return False
            i += 1
        if flag_dot and not flag_num:
            return False
        if flag_e and not flag_num:
            return False
        return True

if __name__ == "__main__":
    s = "  1.1e  "
    print(Solution().isNumber(s))
