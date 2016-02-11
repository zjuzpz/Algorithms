"""
255. Verify Preorder Sequence in Binary Search Tree
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?
"""
# Look the nums one by one, and if we find a num is larger than another one, all
# the following nums should all larger than the smaller one
# O(n)
# O(h)
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack, smallest = [], -float("inf")
        for i in range(len(preorder)):
            if not stack or preorder[i] < stack[-1]:
                if preorder[i] < smallest:
                    return False
            else:
                while stack and stack[-1] < preorder[i]:
                    smallest = stack.pop()
            stack.append(preorder[i])
        return True

# O(n)
# O(1)
class Solution2(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        i, smallest = -1, -float("inf")
        for num in preorder:
            if num < smallest:
                return False
            while i >= 0 and num > preorder[i]:
                smallest = preorder[i]
                i -= 1
            i += 1
            preorder[i] = num
        return True

if __name__ == "__main__":
    print(Solution().verifyPreorder([2, 3, 1]))
