
public class RecoverBinarySearchTree {
    public void recoverTree(TreeNode root) {
        TreeNode first = null;
        TreeNode second = null;
        TreeNode cur = root;
        TreeNode prev = new TreeNode(Integer.MIN_VALUE);
        TreeNode tem;
        while(cur != null) {
            if(cur.left == null) {
                if(cur.val < prev.val) {
                    if(first == null) {
                        first = prev;
                    }
                    second = cur;
                }
                prev = cur;
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
                    if(cur.val < prev.val) {
                        if(first == null) {
                            first = prev;
                        }
                        second = cur;
                    }
                    prev = cur;
                    cur = cur.right;
                    tem.right = null;
                }
            }
        }
        int temVal = first.val;
        first.val = second.val;
        second.val = temVal;
    }
    
    public static void main(String[] args) {
    	TreeNode root = new TreeNode(3);
    	root.right = new TreeNode(1);
    	root.right.left = new TreeNode(2);
    	new RecoverBinarySearchTree().recoverTree(root);
    }

}
