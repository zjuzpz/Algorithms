
public class MaximumProductSubarray {
    public int maxProduct(int[] nums) {
        int globalMax = nums[0];
        int localMax = nums[0];
        int localMin = nums[0];
        int tem;
        for(int i = 1; i < nums.length; i++) {
            tem = localMax;
            localMax = Math.max(localMax * nums[i], Math.max(localMin * nums[i], nums[i]));
            localMin = Math.min(tem * nums[i], Math.min(localMin * nums[i], nums[i]));
            globalMax = Math.max(globalMax, localMax);
        }
        return globalMax;
    }

}
