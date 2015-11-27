"""
119. Pascal's Triangle II
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
# O(n ^ 2)
# O(n)
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        while rowIndex > 0:
            rowIndex -= 1
            tem = []
            for i in range(len(res) + 1):
                if i == 0 or i == len(res):
                    tem.append(1)
                else:
                    tem.append(res[i - 1] + res[i])
            res = tem
        return res

if __name__ == "__main__":
    print(Solution().getRow(5))
