import java.util.*;
public class BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> vals;
        List<TreeNode> cur = new ArrayList<TreeNode>();
        List<TreeNode> next;
        if(root == null) {return res;}
        cur.add(root);
        while(cur.size() != 0) {
            vals = new ArrayList<Integer>();
            next = new ArrayList<TreeNode>();
            for(TreeNode node: cur) {
                vals.add(node.val);
                if(node.left != null) {next.add(node.left);}
                if(node.right != null) {next.add(node.right);}
            }
            res.add(vals);
            cur = next;
        }
        return res;
    }

}
