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
        if n <= 0:
            return []
        res = []
        if n % 2 == 1:
            self.find(res, [], n // 2, True)
        else:
            self.find(res, [], n // 2, False)
        return res
        
    def find(self, res, cur, length, mid):
        if len(cur) == length:
            right = self.getRight(cur)
            if mid:
                res.append("".join(cur + ["0"] + right))
                res.append("".join(cur + ["1"] + right))
                res.append("".join(cur + ["8"] + right))
            else:
                res.append("".join(cur + right))
            return
        if len(cur) != 0:
            cur.append("0")
            self.find(res, cur, length, mid)
            cur.pop()
        for i in ["1", "6", "8", "9"]:
            cur.append(i)
            self.find(res, cur, length, mid)
            cur.pop()
            
    def getRight(self, l):
        res = []
        for i in l:
            if i in ["0", "1", "8"]:
                res.append(i)
            elif i == "6":
                res.append("9")
            else:
                res.append("6")
        res.reverse()
        return res

if __name__ == "__main__":
    print(Solution().findStrobogrammatic(7))
