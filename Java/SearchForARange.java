
public class SearchForARange {
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[]{-1, -1};
        if(nums == null || nums.length == 0) {return res;}
        int lower = 0;
        int upper = nums.length - 1;
        int left = binarySearch(lower, upper, nums, target, true);
        if(nums[left] != target) {return res;}
        res[0] = left;
        int right = binarySearch(lower, upper, nums, target, false);
        if(nums[right] == target) {
            res[1] = right;
        } else {
            res[1] = right - 1;
        }
        return res;
    }
    
    private int binarySearch(int lower, int upper, int[] nums, int target, boolean isLeft) {
        int mid;
        while(lower < upper) {
            mid = lower + (upper - lower) / 2;
            if(nums[mid] < target) {
                lower = mid + 1;
            } else if(nums[mid] > target){
                upper = mid - 1;
            } else {
                if(isLeft) {
                    upper = mid;
                } else {
                    lower = mid + 1;
                }
            }
        }
        return lower;
    }

}
