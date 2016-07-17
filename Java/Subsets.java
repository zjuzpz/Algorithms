import java.util.*;
public class Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();
        recur(res, cur, nums, 0);
        return res;
    }
    
    private void recur(List<List<Integer>> res, List<Integer> cur, int[] nums, int start) {
        if(start == nums.length) {
            res.add(new ArrayList<Integer>(cur));
            return;
        }
        recur(res, cur, nums, start + 1);
        cur.add(nums[start]);
        recur(res, cur, nums, start + 1);
        cur.remove(cur.size() - 1);
    }

}
