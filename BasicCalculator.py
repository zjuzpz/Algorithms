"""
224. Basic Calculator
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
"""
# O(n)
# O(n)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign, stack = 0, 0, 1, []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in "+-":
                res += num * sign
                num = 0
                sign = 1 if s[i] == "+" else -1
            elif s[i] == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif s[i] == ")":
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign

if __name__ == "__main__":
    s = "2-4-(8+2-6+(8+4-(1)+8-10))"
    s = "(2-3) + 8"
    s = " 123"
    print(Solution().calculate(s))
    print(eval(s))
