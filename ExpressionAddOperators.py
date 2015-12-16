"""
282. Expression Add Operators
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""
# O(4 ^ n)
# O(n)
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        val, str_val, res = 0, "", []
        for i in range(len(num)):
            val = val * 10 + int(num[i])
            str_val += num[i]
            if str(val) != str_val:
                break
            self.recur(i + 1, res, str_val, 0, val, num, target)
        return res
        
    def recur(self, pos, res, cur, num1, num2, num, target):
        if pos == len(num):
            if num1 + num2 == target:
                res.append(cur)
        else:
            val, str_val = 0, ""
            for i in range(pos, len(num)):
                val = val * 10 + int(num[i])
                str_val += num[i]
                if str(val) != str_val:
                    break
                self.recur(i + 1, res, cur + "+" + str_val, num1 + num2, val, num, target)
                self.recur(i + 1, res, cur + "-" + str_val, num1 + num2, -val, num, target)
                self.recur(i + 1, res, cur + "*" + str_val, num1, num2 * val, num, target)


if __name__ == "__main__":
    num = "3456237490"
    target = 9191
    print(Solution().addOperators(num, target))
