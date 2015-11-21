"""
150. Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
# O(n)
# O(n)
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                right = stack.pop()
                opt = tokens[i]
                left = stack.pop()
                res = self.myOpt(left, opt, right)
                stack.append(res)
            else:
                stack.append(tokens[i])
        return int(stack[0])

#When do /, for python 2, it needs to convert at least one int to float
#For python 3, can do int(left / right), and note cannot do int(left) // int(right)
#because -3 // 5 will be -1 other than 0
        
    def myOpt(self, left, opt, right):
        if opt == "+":
            return int(left) + int(right)
        if opt == "-":
            return int(left) - int(right)
        if opt == "*":
            return int(left) * int(right)
        return int(float(left) / float(right))
    
if __name__ == "__main__":
    print (Solution().evalRPN(["5", "7", "5", "/", "*"]))
    print (Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


