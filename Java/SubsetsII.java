import java.util.*;
public class SubsetsII {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();
        recur(cur, res, nums, 0);
        return res;
    }
    
    private void recur(List<Integer> cur, List<List<Integer>> res, int[] nums, int start) {
        res.add(new ArrayList<Integer>(cur));
        int i = start;
        while(i < nums.length) {
            cur.add(nums[i]);
            recur(cur, res, nums, i + 1);
            cur.remove(cur.size() - 1);
            i++;
            while(i < nums.length && nums[i] == nums[i - 1]) {
                i++;
            }
        }
    }

}
