"""
241. Different Ways to Add Parentheses
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""
# O(n * 4 ^ n / n ^ (3 / 2))
# O(n * 4 ^ n / n ^ (3 / 2))
# Catalan Number: h(n) = h(n - 1) * (4 * n - 2) / (n + 1)
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if not input:
            return []
        l, tem = [], ""
        for i in range(len(input)):
            if input[i].isdigit():
                tem += input[i]
            else:
                l.append(int(tem))
                l.append(input[i])
                tem = ""
        l.append(int(tem))
        return self.recur(l)
        
    def recur(self, l):
        if len(l) == 1:
            return l
        res = []
        for i in range(1, len(l), 2):
            left = self.recur(l[0 : i])
            right = self.recur(l[i + 1 :])
            for j in left:
                for k in right:
                    res.append(self.opt(j, l[i], k)) 
        return res
    
    def opt(self, num1, operator, num2):
        if operator == "+":
            return num1 + num2
        if operator == "-":
            return num1 - num2
        return num1 * num2

if __name__ == "__main__":
    input = "1"
    for i in range(8):
        print(len(Solution().diffWaysToCompute(input)))
        input += "+1"
