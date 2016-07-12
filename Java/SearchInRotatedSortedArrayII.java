
public class SearchInRotatedSortedArrayII {
    public boolean search(int[] nums, int target) {
        int lower = 0;
        int upper = nums.length - 1;
        int mid;
        while(lower <= upper) {
            mid = (lower + upper) / 2;
            if(nums[mid] == target) {return true;}
            if(nums[mid] > nums[lower]) {
                if(nums[mid] > target && nums[lower] <= target) {
                    upper = mid - 1;
                } else {
                    lower = mid + 1;
                }
            } else if(nums[mid] < nums[lower]) {
                if(nums[mid] < target && nums[upper] >= target) {
                    lower = mid + 1;
                } else {
                    upper = mid - 1;
                }
            } else {
                lower++;
            }
        }
        return false;
    }

}
