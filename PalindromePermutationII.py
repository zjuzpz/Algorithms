"""
267. Palindrome Permutation II
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].
"""
# O(n * n!)
# O(n)
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        lookup = {}
        for i in s:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        single, l = None, []
        for key in lookup:
            if lookup[key] % 2 == 1:
                if single is None:
                    single = key
                else:
                    return []
            tem = [key for i in range(lookup[key] // 2)]
            l += tem
        res = []
        p = self.generate(l, single)
        res.append(p)
        initial = l[:]
        l = self.nextPerm(l)
        while l != initial:
            p = self.generate(l ,single)
            res.append(p)
            l = self.nextPerm(l)
        return res
        
    def generate(self, l, single):
        left = l
        right = l[:]
        right.reverse()
        if single:
            return "".join(left + [single] + right)
        return "".join(left + right)
        
    def nextPerm(self, l):
        index = None
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                index = i
        if index is None:
            return l[::-1]
        for i in range(index + 1, len(l)):
            if l[index] < l[i]:
                change = i
            else:
                break
        l[index], l[change] = l[change], l[index]
        c = l[index + 1:][:]
        c.reverse()
        return l[0 : index + 1] + c

if __name__ == "__main__":
    s = "abcca"
    print(Solution().generatePalindromes(s))
