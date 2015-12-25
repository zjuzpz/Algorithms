"""
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
# O(n)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        if not root:
            return data
        cur = [root]
        while cur:
            next = []
            for node in cur:
                if node:
                    data.append(node.val)
                    next.append(node.left)
                    next.append(node.right)
                else:
                    data.append(None)
            cur = next
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return 
        root = TreeNode(data[0])
        cur = [root]
        i = 1
        while i < len(data):
            next = []
            for node in cur:
                if data[i] is not None:
                    node.left = TreeNode(data[i])
                    next.append(node.left)
                i += 1
                if data[i] is not None:
                    node.right = TreeNode(data[i])
                    next.append(node.right)
                i += 1
            cur = next
        return root
        

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    codec = Codec()
    c = codec.serialize(root)
    print(c)
    r = codec.deserialize(c)
    print(root.val, root.left.val, root.right.val, root.right.left.val)
