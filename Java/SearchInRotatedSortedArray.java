
public class SearchInRotatedSortedArray {
    public int search(int[] nums, int target) {
        int lower = 0;
        int upper = nums.length - 1;
        int mid;
        while(lower <= upper) {
            mid = lower + (upper - lower) / 2;
            if(nums[mid] == target) {return mid;}
            if(nums[mid] >= nums[lower]) {
                if(target >= nums[lower] && target < nums[mid]) {
                    upper = mid - 1;
                } else {
                    lower = mid + 1;
                }
            } else {
                if(target > nums[mid] && target <= nums[upper]) {
                    lower = mid + 1;
                } else {
                    upper = mid - 1;
                }
            }
        }
        return -1;
    }

}
