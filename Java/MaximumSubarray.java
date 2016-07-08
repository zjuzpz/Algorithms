
public class MaximumSubarray {
    public int maxSubArray(int[] nums) {
        int localMax = nums[0];
        int globalMax = nums[0];
        for(int i = 1; i < nums.length; i++) {
            localMax = Math.max(localMax + nums[i], nums[i]);
            globalMax = Math.max(globalMax, localMax);
        }
        return globalMax;
    }

}
