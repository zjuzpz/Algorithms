
public class MajorityElement {
    public int majorityElement(int[] nums) {
        int cur = nums[0];
        int count = 1;
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] == cur) {count++;}
            else {
                count--;
                if(count == 0) {
                    cur = nums[i];
                    count = 1;
                }
            }
        }
        return cur;
    }

}
