import java.util.*;
public class ContainsDuplicateIII {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if(t < 0 || k <= 0) {return false;}
        Map<Integer, Integer> buckets = new HashMap<Integer, Integer>();
        int bucket;
        int[] neighbors;
        for(int i = 0; i < nums.length; i++) {
            if(buckets.size() > k) {
                bucket = (t == 0)? nums[i - k - 1] : nums[i - k - 1] / t;
                buckets.remove(bucket);
            }
            bucket = (t == 0) ? nums[i] : nums[i] / t;
            neighbors = new int[]{bucket - 1, bucket, bucket + 1};
            for(int neighbor: neighbors) {
                if(buckets.containsKey(neighbor) && Math.abs(new Long(buckets.get(neighbor) - nums[i])) <= t) {
                    return true;
                }
            }
            buckets.put(bucket, nums[i]);
        }
        return false;
    }
    
    public static void main(String[] args) {
    	int[] nums = {-1, Integer.MAX_VALUE};
    	int k = 1;
    	int t = Integer.MAX_VALUE;
    	System.out.println(new ContainsDuplicateIII().containsNearbyAlmostDuplicate(nums, k, t));
    }

}
