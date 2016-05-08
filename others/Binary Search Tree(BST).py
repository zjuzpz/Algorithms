"""
Binary Search Tree (BST)
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            cur = self.root
            node = TreeNode(val)
            while True:
                if val < cur.val:
                    if not cur.left:
                        cur.left = node
                        node.parent = cur
                        return
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = node
                        node.parent = cur
                        return
                    cur = cur.right

    def search(self, val):
        cur = self.root
        while cur:
            if cur.val == val:
                return cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def delete(self, val):
        node = self.search(val)
        if not node.left or not node.right:
            if node is node.parent.left:
                node.parent.left = node.left or node.right
                if node.parent.left is not None:
                    node.parent.left.parent = node.parent
            else:
                node.parent.right = node.left or node.right
                if node.parent.right is not None:
                    node.parent.right.parent = node.parent
            del(node)
        else:
            tem = node.right
            while tem.left:
                tem = tem.left
            node.val = tem.val
            if tem is tem.parent.left:
                tem.parent.left = None
            else:
                tem.parent.right = None
            del(tem)

    def traversal(self):
        if not self.root:
            return []
        res = []
        self.helper(self.root.left, res)
        res.append(self.root.val)
        self.helper(self.root.right, res)
        return res

    def helper(self, node, res):
        if not node:
            return
        self.helper(node.left, res)
        res.append(node.val)
        self.helper(node.right, res)
        



if __name__ == "__main__":
    bst = BST()
    bst.add(4)
    bst.add(2)
    bst.add(1)
    bst.add(3)
    bst.add(7)
    bst.add(5)
    bst.add(6)
    bst.add(8)
    r = bst.root
    print(bst.traversal())
    bst.delete(6)
    print(bst.traversal())
    bst.delete(7)
    print(bst.traversal())
    bst.delete(2)
    print(bst.traversal())
    bst.delete(4)
    print(bst.traversal())
            






            
        
        
