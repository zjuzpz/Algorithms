import java.util.*;

public class Permutation {

    public static List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(nums.length == 0) {return res;}
        List<Integer> cur = new ArrayList<Integer>();
        Set<Integer> visited = new HashSet<Integer>();
        recur(res, cur, visited, nums);
        return res;
    }
    
    public static void recur(List<List<Integer>> res, List<Integer> cur, Set<Integer> visited, int[] nums) {
        if(cur.size() == nums.length) {
            res.add(new ArrayList<Integer>(cur));
            return;
        }
        for(int i = 0; i < nums.length; i++) {
            if(!visited.contains(i)) {
                visited.add(i);
                cur.add(nums[i]);
                recur(res, cur, visited, nums);
                cur.remove(cur.size() - 1);
                visited.remove(i);
            }
        }
    }
    
	
	public static void main(String[] args) {
		int[] nums = {1, 2, 3};
		System.out.println(permute(nums));

	}

}
