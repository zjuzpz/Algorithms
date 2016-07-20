
public class SumRootToLeafNumbers {
    public int sumNumbers(TreeNode root) {
        return helper(0 , root);
    }
    
    private int helper(int cur, TreeNode root) {
        if(root == null) {return cur;}
        if(root.left == null) {return helper(10 * cur + root.val, root.right);}
        if(root.right == null) {return helper(10 * cur + root.val, root.left);}
        return helper(10 * cur + root.val, root.left) + helper(10 * cur + root.val, root.right);
    }

}
