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
        stack_num, stack_opt, tem = [], [], ""
        for i in range(len(s)):
            if s[i].isdigit():
                tem += s[i]
            elif s[i] in "+-*/":
                if stack_opt and stack_opt[-1] in "*/":
                    num1 = stack_num.pop()
                    num2 = int(tem)
                    opt = stack_opt.pop()
                    stack_num.append(self.opt(num1, opt, num2))
                    stack_opt.append(s[i]) 
                    tem = ""
                else:
                    stack_num.append(int(tem))
                    stack_opt.append(s[i])
                    tem = ""
        if stack_opt and stack_opt[-1] in "*/":
            num1 = stack_num.pop()
            num2 = int(tem)
            opt = stack_opt.pop()
            stack_num.append(self.opt(num1, opt, num2))
        else:
            stack_num.append(int(tem))
        res = stack_num[0]
        for i in range(len(stack_opt)):
            res = self.opt(res, stack_opt[i], stack_num[i + 1])
        return res
        
    def opt(self, num1, opt, num2):
        if opt == "+":
            return num1 + num2
        if opt == "-":
            return num1 - num2
        if opt == "*":
            return num1 * num2
        if num1 * num2 < 0:
            flag = -1
        else:
            flag = 1
        return flag * (abs(num1) // abs(num2))

if __name__ == "__main__":
    print(Solution().calculate("3+2*2"))
