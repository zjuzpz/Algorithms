
public class WiggleSubsequence {
    public int wiggleMaxLength(int[] nums) {
        if(nums.length == 0) {return 0;}
        int res = 1;
        res = Math.max(res, helper(nums, true));
        return Math.max(res, helper(nums, false));
    }
    
    private int helper(int[] nums, boolean isLarger) {
        int res = 1;
        int cur = nums[0];
        for(int i = 1; i < nums.length; i++) {
            if(isLarger && nums[i] > cur) {
                res++;
                isLarger = false;
            } else if(!isLarger && nums[i] < cur) {
                res++;
                isLarger = true;
            }
            cur = nums[i];
        }
        return res;
    }

}
