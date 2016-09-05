
public class JumpGame {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        for(int i = 0; i < nums.length; i++) {
            if(i > maxReach) {
                return false;
            } else {
                maxReach = Math.max(maxReach, i + nums[i]);
            }
        }
        return true;
    }

}
