
public class SearchInsertPosition {
    public static int searchInsert(int[] nums, int target) {
        int lower = 0;
        int upper = nums.length - 1;
        int mid;
        while(lower <= upper) {
            mid = (lower + upper) / 2;
            if(nums[mid] == target) {return mid;}
            if(nums[mid] < target) {
                lower = mid + 1;
            } else {
                upper = mid - 1;
            }
        }
        return lower;
    }

	public static void main(String[] args) {
		int[] nums = {1, 3, 5, 6};
		System.out.println(searchInsert(nums, 5));
		System.out.println(searchInsert(nums, 2));
		System.out.println(searchInsert(nums, 7));
		System.out.println(searchInsert(nums, 0));
	}

}
