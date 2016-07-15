import java.util.*;
public class MajorityElementII {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<Integer>();
        int[] twoNums = new int[2];
        int[] count = new int[2];
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == twoNums[0]) {
                count[0]++;
            } else if(nums[i] == twoNums[1]) {
                count[1]++;
            } else if(count[0] == 0) {
                twoNums[0] = nums[i];
                count[0] = 1;
            } else if(count[1] == 0) {
                twoNums[1] = nums[i];
                count[1] = 1;
            } else {
                count[0]--;
                count[1]--;
            }
        }
        count[0] = 0;
        count[1] = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == twoNums[0]) {
                count[0]++;
            } else if(nums[i] == twoNums[1]) {
                count[1]++;
            }
        }
        if(count[0] > nums.length / 3) {res.add(twoNums[0]);}
        if(count[1] > nums.length / 3) {res.add(twoNums[1]);}
        return res;
    }

}
