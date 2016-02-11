"""
227. Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
"""
# O(n)
# O(n)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stackNum, stackOpt, tem = [], [], ""
        for i in range(len(s)):
            if s[i] in "+-*/":
                stackNum.append(int(tem))
                tem = ""
                if stackOpt and stackOpt[-1] in "*/":
                    stackNum.append(self.opter(stackNum.pop(), stackOpt.pop(), stackNum.pop()))
                stackOpt.append(s[i])
            else:
                tem += s[i]
        stackNum.append(int(tem))
        if stackOpt and stackOpt[-1] in "*/":
            stackNum.append(self.opter(stackNum.pop(), stackOpt.pop(), stackNum.pop()))
        res = stackNum[0]
        for i in range(len(stackOpt)):
            res = self.opter(stackNum[i + 1], stackOpt[i], res)
        return res
        
    def opter(self, num2, opt, num1):
        if opt == "+":
            return num1 + num2
        if opt == "-":
            return num1 - num2
        if opt == "*":
            return num1 * num2
        return num1 // num2

if __name__ == "__main__":
    print(Solution().calculate("3+2*2"))
