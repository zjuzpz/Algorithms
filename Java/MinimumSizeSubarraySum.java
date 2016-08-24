
public class MinimumSizeSubarraySum {
    public int minSubArrayLen(int s, int[] nums) {
        int i = 0;
        int j = 0;
        int sum = 0;
        int res = nums.length + 1;
        while(j < nums.length || sum >= s) {
            if(sum >= s) {
                res = Math.min(res, j - i);
                sum -= nums[i];
                i++;
            } else {
                sum += nums[j];
                j++;
            }
        }
        if(res == nums.length + 1) {return 0;}
        return res;
    }

}
