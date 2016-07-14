
public class IncreasingTripletSubsequence {
    public boolean increasingTriplet(int[] nums) {
        if(nums.length < 3) {return false;}
        int[] lookup = new int[2];
        lookup[0] = nums[0];
        lookup[1] = Integer.MAX_VALUE;
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] <= lookup[0]) {
                lookup[0] = nums[i];
            } else if(nums[i] <= lookup[1]) {
                lookup[1] = nums[i];
            } else {
                return true;
            }
        }
        return false;
    }

}
