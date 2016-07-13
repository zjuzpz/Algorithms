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

#add a new node in the bst
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

#search if the value in the bst, if it is, return the node, else return False
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

#delete a value in the bst, if the value not in the bst, return False, otherwise
#return True
    def delete(self, val):
        node = self.search(val)
        if not node:
            return False
        #If the node just have one child or have no child
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
        #The node have two children
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
        return True
    
#Morris travelsal of the tree, whose space complexity is O(1)
    def traversal(self):
        if not self.root:
            return []
        cur = self.root
        res = []
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                tem = cur.left
                while tem.right and tem.right != cur:
                    tem = tem.right
                if not tem.right:
                    tem.right = cur
                    cur = cur.left
                else:
                    res.append(cur.val)
                    cur = cur.right
                    tem.right = None
        return res


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
            






            
        
        
