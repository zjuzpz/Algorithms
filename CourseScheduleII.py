"""
210. Course Schedule II
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3].
Another correct ordering is[0,2,1,3].
"""
# O(n)
# O(n)
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        lookup, pre = {}, prerequisites
        for i in range(len(pre)):
            if pre[i][0] not in lookup:
                lookup[pre[i][0]] = [pre[i][1]]
            else:
                lookup[pre[i][0]].append(pre[i][1])
        learnt, res = set(), []
        for i in range(numCourses):
            if i not in lookup:
                learnt.add(i)
                res.append(i)
        for key in lookup:
            visited = set()
            visited.add(key)
            if not self.recur(res, lookup, visited, learnt, key):
                return []
            if key not in learnt:
                learnt.add(key)
                res.append(key)
        return res
        
    def recur(self, res, lookup, visited, learnt, key):
        for pre in lookup[key]:
            if pre in visited:
                return False
            if pre not in learnt:
                visited.add(pre)
                if not self.recur(res, lookup, visited, learnt, pre):
                    return False
                if pre not in learnt:
                    learnt.add(pre)
                    res.append(pre)
                visited.remove(pre)
        return True

if __name__ == "__main__":
    n = 4
    p = [[1,0], [2,0], [3,1], [3,2]]
    print(Solution().findOrder(n, p))
