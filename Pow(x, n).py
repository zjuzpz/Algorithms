"""
50. Implement pow(x, n).
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        flag_n, flag_x = 1, 1
        if n == 0:
            return 1
        if  n < 0:
            n = -n
            flag_n = -1
        if x < 0:
            x = -x
            if n % 2 == 1:
                flag_x = -1
        cur, res = x, 1
        while n >= 1:
            rem = n % 2
            if rem == 1:
                res *= cur
            cur *= cur
            n //= 2
        if flag_n == -1:
            return flag_x * 1/res
        return flag_x * res

class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.myPow(x, -n)
        return self.myPowHelper(x, n)
        
    def myPowHelper(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 1:
            return x * self.myPowHelper(x * x, n // 2)
        return self.myPowHelper(x * x, n // 2)

if __name__ == "__main__":
    print(Solution().myPow(2.3, -1))
