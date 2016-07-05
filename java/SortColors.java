import java.util.Arrays;


public class SortColors {

    public static void sortColors(int[] nums) {
        int i = 0;
        int j = nums.length - 1;
        while(i <= j) {
            if(nums[i] == 0) {
                i++;
            } else if(nums[i] == 1) {
                break;
            } else {
                nums[i] = nums[j];
                nums[j] = 2;
                j--;
            }
        }
        int firstOne = i;
        i++;
        while(i <= j) {
            if(nums[i] == 0) {
                nums[i] = 1;
                nums[firstOne] = 0;
                firstOne++;
                i++;
            } else if(nums[i] == 1) {
                i++;
            } else {
                nums[i] = nums[j];
                nums[j] = 2;
                j--;
            }
        }
    }
    
	public static void main(String[] args) {
		int[] nums = {1, 0, 2, 2, 1, 0, 1, 1, 2, 2, 0, 0};
		sortColors(nums);
		System.out.println(Arrays.toString(nums));

	}

}
