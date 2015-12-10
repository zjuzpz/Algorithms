"""
71. Simplify Path
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""
# O(n)
# O(1)
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tokens, res = path.split("/"), []
        for token in tokens:
            if token == "..":
                if res:
                    res.pop()
            elif token != "." and token != "":
                res.append(token)
        return "/" + "/".join(res)
if __name__ == "__main__":
    path1 = '/a/./b/../../c/'
    path2 = '/...'
    path3 = '/home//foo/'
    path4 = '/a/../b/'
    print(Solution().simplifyPath(path2))
