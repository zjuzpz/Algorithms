import java.util.*;
public class BinaryTreeZigzagLevelOrderTraversal {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(root == null) {return res;}
        List<Integer> vals;
        List<TreeNode> cur = new ArrayList<TreeNode>();
        List<TreeNode> next;
        cur.add(root);
        boolean flag = true;
        while(cur.size() != 0) {
            next = new ArrayList<TreeNode>();
            vals = new ArrayList<Integer>();
            for(TreeNode node: cur) {
                vals.add(node.val);
                if(node.left != null) {next.add(node.left);}
                if(node.right != null) {next.add(node.right);}
            }
            cur = next;
            if(flag) {
                res.add(vals);
                flag = false;
            } else {
                Collections.reverse(vals);
                res.add(vals);
                flag = true;
            }
        }
        return res;
    }

}
