import java.util.*;
public class LongestIncreasingSubsequence {
    public int lengthOfLIS(int[] nums) {
        if(nums.length == 0) {return 0;}
        int[] dp = new int[nums.length];
        int res = 1;
        Arrays.fill(dp, 1);
        for(int i = 1; i < nums.length; i++) {
            for(int j = 0; j < i; j++) {
                if(nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            res = Math.max(res, dp[i]);
        }
        return res;
    }
    
    public int lengthOfLIS2(int[] nums) {
        if(nums.length == 0) {return 0;}
        List<Integer> res = new ArrayList<Integer>();
        res.add(nums[0]);
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] > res.get(res.size() - 1)) {
                res.add(nums[i]);
            } else {
                res.set(binarySearch(res, nums[i]), nums[i]);
            }
        }
        return res.size();
    }
    
    private int binarySearch(List<Integer> nums, int target) {
        int lower = 0;
        int upper = nums.size() - 1;
        int mid;
        while(lower < upper) {
            mid = lower + (upper - lower) / 2;
            if(nums.get(mid) == target) {
                return mid;
            }
            if(nums.get(mid) < target) {
                lower = mid + 1;
            } else {
                upper = mid;
            }
        }
        return lower;
    }

}
