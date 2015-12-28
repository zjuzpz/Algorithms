"""
247. Strobogrammatic Number II
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
"""
# O(n^2 * 5^(n/2))
# O(n)
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n % 2 == 1:
            mid = True
        else:
            mid = False
        self.generate(res, [], n // 2, mid)
        return res
        
    def generate(self, res, cur, length, mid):
        if len(cur) == length:
            res.extend(self.helper(cur, mid))
            return
        if len(cur) == 0:
            for i in ("1", "6", "8", "9"):
                cur.append(i)
                self.generate(res, cur, length, mid)
                cur.pop()
        else:
            for i in ("0", "1", "6", "8", "9"):
                cur.append(i)
                self.generate(res, cur, length, mid)
                cur.pop()
                
    def helper(self, left, mid):
        res, right = [], []
        for i in reversed(range(len(left))):
            if left[i] in ("0", "1", "8"):
                right.append(left[i])
            elif left[i] == "6":
                right.append("9")
            else:
                right.append("6")
        if mid:
            for i in ("0", "1", "8"):
                tem = left + [i] + right
                res.append("".join(tem))
        else:
            tem = left + right
            res.append("".join(tem))
        return res

if __name__ == "__main__":
    print(Solution().findStrobogrammatic(7))
