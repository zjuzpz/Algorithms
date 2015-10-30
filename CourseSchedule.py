"""
207. Course Schedule
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:
2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
# O(E + V)
# O(E)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pre, lookup, visited = prerequisites, {}, []
        for i in range(len(pre)):
            if pre[i][0] not in lookup:
                lookup[pre[i][0]] = [pre[i][1]]
            else:
                lookup[pre[i][0]].append(pre[i][1])
        if not lookup:
            return True
        learnt = set()
        for i in lookup:
            visited = set()
            if not self.BFS(lookup, visited, i, learnt):
                return False
        return True
        
    def BFS(self, lookup, visited, course, learnt):
        for i in lookup[course]:
            if i in visited:
                return False
            if i not in learnt and i in lookup:
                visited.add(i)
                if not self.BFS(lookup, visited, i, learnt):
                    return False
                visited.remove(i)
        learnt.add(course)
        return True

if __name__ == "__main__":
    pre = [[1,0], [0,1]]
    print(Solution().canFinish(2, pre))
