
public class JumpGameII {
    public int jump(int[] nums) {
        int reached = 0;
        int nextStepReached = nums[0];
        int steps = 0;
        for(int i = 1; i < nums.length; i++) {
            if(i > reached) {
                reached = nextStepReached;
                steps++;
            }
            nextStepReached = Math.max(nextStepReached, i + nums[i]);
        }
        return steps;
    }

}
