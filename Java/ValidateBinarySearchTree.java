import java.util.*;

public class ValidateBinarySearchTree {
    public boolean isValidBST(TreeNode root) {
        int prev = Integer.MIN_VALUE;
        boolean flag = false;
        TreeNode cur = root;
        TreeNode tem;
        while(cur != null) {
            if(cur.left == null) {
                if(cur.val < prev) {return false;}
                if(cur.val == prev) {
                    if(prev != Integer.MIN_VALUE || flag) {return false;}
                    flag = true;
                }
                prev = cur.val;
                cur = cur.right;
            } else {
                tem = cur.left;
                while(tem.right != null && tem.right != cur){
                    tem = tem.right;
                }
                if(tem.right == null) {
                    tem.right = cur;
                    cur = cur.left;
                } else {
                    if(cur.val < prev) {return false;}
                    if(cur.val == prev) {
                        if(prev != Integer.MIN_VALUE || flag) {return false;}
                        flag = true;
                    }
                    prev = cur.val;
                    cur = cur.right;
                    tem.right = null;
                }
            }
        }
        return true;
    }
    
    public boolean isValidBST2(TreeNode root) {
        if(root == null) {return true;}
        int prev = Integer.MIN_VALUE;
        boolean flag = false;
        TreeNode cur = root.left;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.add(root);
        while(stack.size() != 0 || cur != null) {
            if(cur != null) {
                stack.add(cur);
                cur = cur.left;
            } else {
                cur = stack.pop();
                if(cur.val < prev) {return false;}
                if(cur.val == prev) {
                    if(cur.val != Integer.MIN_VALUE || flag) {return false;}
                    flag = true;
                }
                prev = cur.val;
                cur = cur.right;
            }
        }
        return true;
    }

}
