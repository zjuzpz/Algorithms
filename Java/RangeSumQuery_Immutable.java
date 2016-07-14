
public class RangeSumQuery_Immutable {
	class NumArray {
	    int[] res;

	    public NumArray(int[] nums) {
	        res = new int[nums.length + 1];
	        res[0] = 0;
	        for(int i = 0; i < nums.length; i++) {
	            res[i + 1] = res[i] + nums[i];
	        }
	    }

	    public int sumRange(int i, int j) {
	        return res[j + 1] - res[i];
	    }
	}

}
