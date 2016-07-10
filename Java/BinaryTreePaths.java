import java.util.*;

public class BinaryTreePaths {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<String>();
        Stack<String> cur = new Stack<String>();
        if(root == null) {return res;}
        recur(res, cur, root);
        return res;
    }
    
    public void recur(List<String> res, Stack<String> cur, TreeNode node) {
        cur.add(Integer.toString(node.val));
        if(node.left == null && node.right == null) {
            res.add(String.join("->", cur));
            cur.pop();
            return;
        }
        if(node.left != null) {
            recur(res, cur, node.left);
        }
        if(node.right != null) {
            recur(res, cur, node.right);
        }
        cur.pop();
    }

}
