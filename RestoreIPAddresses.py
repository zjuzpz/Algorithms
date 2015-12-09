"""
93. Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
# O(1) (O(3 ^ 4))
# O(1) (O(3 * 4))
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.recur(res, s, 0, len(s), [])
        return res
        
    def recur(self, res, s, start, end, cur):
        if len(cur) == 4:
            if start == end:
                res.append(".".join(cur))
            return
        if start >= end:
            return
        if s[start] == "0":
            cur.append("0")
            self.recur(res, s, start + 1, end, cur)
            cur.pop()
            return
        for i in range(3):
            tem = s[start : start + i + 1]
            if int(tem) <= 255:
                cur.append(tem)
                self.recur(res, s, start + i + 1, end, cur)
                cur.pop()

if __name__ == "__main__":
    print(Solution().restoreIpAddresses("010010"))
