
public class FindMinimumInRotatedSortedArrayII {
    public int findMin(int[] nums) {
        int lower = 0;
        int upper = nums.length - 1;
        int mid;
        while(lower < upper) {
            mid = lower + (upper - lower) / 2;
            if(nums[mid] > nums[lower]) {
                if(nums[upper] > nums[lower]) {return nums[lower];}
                else {lower = mid + 1;}
            } else if(nums[mid] < nums[lower]) {
                upper = mid;
            } else {
                lower++;
            }
        }
        if(lower != 0 && nums[lower] > nums[lower - 1]) {return nums[lower - 1];}
        return nums[lower];
    }

}
