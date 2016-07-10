import java.util.*;
public class KthSmallestElementInABST {
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode cur = root;
        while(true) {
            if(cur != null) {
                stack.add(cur);
                cur = cur.left;
            } else {
                cur = stack.pop();
                k--;
                if(k == 0) {return cur.val;}
                cur = cur.right;
            }
        }
    }
    
    public int kthSmallest2(TreeNode root, int k) {
        TreeNode cur = root;
        TreeNode tem;
        while(cur != null) {
            if(cur.left == null) {
                k--;
                if(k == 0) {return cur.val;}
                cur = cur.right;
            } else {
                tem = cur.left;
                while(tem.right != null && tem.right != cur) {
                    tem = tem.right;
                }
                if(tem.right == null) {
                    tem.right = cur;
                    cur = cur.left;
                } else {
                    k--;
                    if(k == 0) {
                        tem.right = null;
                        return cur.val;
                    }
                    cur = cur.right;
                    tem.right = null;
                }
            }
        }
        return -1;
    }

}
