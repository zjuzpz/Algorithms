import java.util.Arrays;


public class NextPermutation {
	
    public static void nextPermutation(int[] nums) {
        if(nums.length == 0) {return;}
        int index = -1;
        int i = 1;
        while(i < nums.length) {
            if(nums[i - 1] < nums[i]) {
                index = i - 1;
            }
            i++;
        }
        if(index == -1) {
            reverseArray(nums, 0, nums.length - 1);
            return;
        }
        int right= index + 1;
        for(int j = right + 1; j < nums.length; j++) {
            if(nums[j] > nums[index]) {
                right = j;
            }
        }
        int tem = nums[index];
        nums[index] = nums[right];
        nums[right] = tem;
        reverseArray(nums, index + 1, nums.length - 1);
    }
    
    public static void reverseArray(int[] nums, int start, int end) {
        int tem;
        while(start < end) {
            tem = nums[start];
            nums[start] = nums[end];
            nums[end] = tem;
            start++;
            end--;
        }
    }

	public static void main(String[] args) {
		int[] nums = {1, 1, 5};
		nextPermutation(nums);
		System.out.println(Arrays.toString(nums));

	}

}
