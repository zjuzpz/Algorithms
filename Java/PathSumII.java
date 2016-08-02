import java.util.*;
public class PathSumII {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();
        if(root == null) {return res;}
        recur(root, res, cur, sum);
        return res;
    }
    
    private void recur(TreeNode node, List<List<Integer>> res, List<Integer> cur, int sum) {
        cur.add(node.val);
        sum -= node.val;
        if(node.left == null && node.right == null) {
            if(sum == 0) {res.add(new ArrayList<Integer>(cur));}
        }
        if(node.left != null) {recur(node.left, res, cur, sum);}
        if(node.right != null) {recur(node.right, res, cur, sum);}
        cur.remove(cur.size() - 1);
    }

}
