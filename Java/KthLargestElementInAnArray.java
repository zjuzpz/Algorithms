import java.util.*;
public class KthLargestElementInAnArray {
    public int findKthLargest(int[] nums, int k) {
        Random r = new Random();
        int lower = 0;
        int upper = nums.length - 1;
        int idx;
        int newIdx;
        while(lower <= upper) {
            idx = r.nextInt(upper - lower + 1) + lower;
            newIdx = partition(idx, lower, upper, nums);
            if(newIdx == nums.length - k) {return nums[newIdx];}
            if(newIdx < nums.length - k) {
                lower = newIdx + 1;
            } else {
                upper = newIdx - 1;
            }
        }
        return -1;
    }
    
    private int partition(int idx, int lower, int upper, int[] nums) {
        int tem = nums[idx];
        nums[idx] = nums[upper];
        nums[upper] = tem;
        int newIdx = lower;
        for(int i = lower; i < upper; i++) {
            if(nums[i] < nums[upper]) {
                tem = nums[newIdx];
                nums[newIdx] = nums[i];
                nums[i] = tem;
                newIdx++;
            }
        }
        tem = nums[upper];
        nums[upper] = nums[newIdx];
        nums[newIdx] = tem;
        return newIdx;
    }

}
