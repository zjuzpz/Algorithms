
public class RotateArray {
    public void rotate(int[] nums, int k) {
        if(nums.length == 0 || k == 0) {return;}
        k = k % nums.length;
        reverse(nums, 0, nums.length);
        reverse(nums, 0, k);
        reverse(nums, k, nums.length);
    }
    
    private void reverse(int[] nums, int start, int end) {
        int i = start;
        int j = end - 1;
        int tem;
        while(i < j) {
            tem = nums[i];
            nums[i] = nums[j];
            nums[j] = tem;
            i++;
            j--;
        }
    }

}
