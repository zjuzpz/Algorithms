
public class LowestCommonAncestorOfABinaryTree {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == p || root == q || root == null) {return root;}
        TreeNode left;
        TreeNode right;
        left = lowestCommonAncestor(root.left, p, q);
        right = lowestCommonAncestor(root.right, p, q);
        if(left != null && right != null) {return root;}
        if(left != null) {return left;}
        return right;
    }

}
