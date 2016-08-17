import java.util.*;


public class BinaryTreeInorderTraversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        TreeNode cur = root;
        TreeNode tem;
        while(cur != null) {
            if(cur.left == null) {
                res.add(cur.val);
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
                    res.add(cur.val);
                    cur = cur.right;
                    tem.right = null;
                }
            }
        }
        return res;
    }

}
