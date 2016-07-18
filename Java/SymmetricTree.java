import java.util.*;
public class SymmetricTree {
    public boolean isSymmetric(TreeNode root) {
        if(root == null) {return true;}
        Stack<TreeNode> left = new Stack<TreeNode>();
        Stack<TreeNode> right = new Stack<TreeNode>();
        left.add(root.left);
        right.add(root.right);
        TreeNode l;
        TreeNode r;
        while(left.size() != 0) {
            l = left.pop();
            r = right.pop();
            if(l == null && r == null) {continue;}
            if(l == null || r == null) {return false;}
            if(l.val != r.val) {return false;}
            left.add(l.left);
            left.add(l.right);
            right.add(r.right);
            right.add(r.left);
        }
        return true;
    }
    
    public boolean isSymmetric2(TreeNode root) {
        if(root == null) {return true;}
        return recur(root.left, root.right);
    }
    
    private boolean recur(TreeNode left, TreeNode right) {
        if(left == null && right == null) {return true;}
        if(left == null || right == null || left.val != right.val) {return false;}
        return recur(left.left, right.right) && recur(left.right, right.left);
    }

}
