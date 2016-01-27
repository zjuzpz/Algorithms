class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MorrisTravesal:
    def preorderTraversal(self, root):
        return
    
    def inorderTraversal(self, root):
        return
        
    def postorderTraversal(self, root):
        dummy = TreeNode(-1)
        dummy.left = root
        res, cur = [], dummy
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                tem = cur.left
                tem_val = [tem.val]
                while tem.right and tem.right != cur:
                    tem = tem.right
                    tem_val.append(tem.val)
                if not tem.right:
                    tem.right = cur
                    cur = cur.left
                else:
                    while tem_val:
                        res.append(tem_val.pop())
                    tem.right = None
                    cur = cur.right
        return res

if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    m = MorrisTravesal()
    print(m.postorderTraversal(root))

