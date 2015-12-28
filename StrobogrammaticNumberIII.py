"""
248. Strobogrammatic Number III
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

Note:
Because the range might be a large number, the low and high numbers are represented as string.
"""
# O(n)
# O(n)
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if float(low) > float(high):
            return 0
        res = 0
        for i in range(len(low) + 1, len(high) + 1):
            res += self.countStrboTotal(i)
        res += self.countStrboRemain(low) - self.countStrboRemain(high)
        return res + 1 if self.isStrbo(high) else res
        
    def countStrboTotal(self, num):
        if num == 0:
            return 0
        mid = 3 if num % 2 == 1 else 1
        num, cur = num // 2, mid
        return cur * 4 * 5 ** (num - 1) if num != 0 else 0
        
    def countStrboRemain(self, s):
        res, lookup, flag = 0, ["0", "1", "6", "8", "9"], True
        for i in range(len(s) // 2):
            if flag:
                for j in range(len(lookup)):
                    if s[i] == lookup[j]:
                        res += (4 - j) * self.helper(len(s) - 2 * (i + 1))
                        break
                    elif s[i] < lookup[j]:
                        res += (5 - j) * self.helper(len(s) - 2 * (i + 1))
                        flag = False
                        break
            else:
                break
        if flag:
            if len(s) % 2 == 1:
                mid = s[len(s) // 2]
                if mid == "0":
                    res += 2
                elif mid < "8":
                    res += 1
                if mid in "018" and self.generate(s) >= s:
                    res += 1
            elif self.generate(s) >= s:
                res += 1
        return res
                    
    def helper(self, num):
        if num == 0:
            return 1
        mid = 3 if num % 2 == 1 else 1
        return mid * 5 ** (num // 2)
        
    def generate(self, s):
        mid, left, right = s[len(s) // 2] if len(s) % 2 == 1 else None, s[0 : len(s) // 2], ""
        for i in reversed(range(len(left))):
            if left[i] in "018":
                right += left[i]
            elif left[i] == "6":
                right += "9"
            else:
                right += "6"
        return left + right if mid is None else left + mid + right
        
    def isStrbo(self, s):
        if len(s) % 2 == 1 and s[len(s) // 2] not in "018":
            return False
        for i in range(len(s) // 2):
            if s[i] in "018":
                if s[len(s) - 1 - i] != s[i]:
                    return False
            elif s[i] == "6":
                if s[len(s) - 1 - i] != "9":
                    return False
            elif s[i] == "9":
                if s[len(s) - 1 - i] != "6":
                    return False
            else:
                return False
        return True

if __name__ == "__main__":
    print(Solution().strobogrammaticInRange("0", "111"))
