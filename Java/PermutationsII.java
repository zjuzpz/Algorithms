import java.util.*;
public class PermutationII {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(nums.length == 0) {return res;}
        Set<List<Integer>> lookup = new HashSet<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();
        boolean[] visited = new boolean[nums.length];
        recur(lookup, cur, visited, nums);
        for(List<Integer> l : lookup) {
            res.add(l);
        }
        return res;
    }
    
    private void recur(Set<List<Integer>> lookup, List<Integer> cur, boolean[] visited, int[] nums) {
        if(nums.length == cur.size()) {
            lookup.add(new ArrayList<Integer>(cur));
            return;
        }
        for(int i = 0; i < nums.length; i++) {
            if(!visited[i]) {
                cur.add(nums[i]);
                visited[i] = true;
                recur(lookup, cur, visited, nums);
                visited[i] = false;
                cur.remove(cur.size() - 1);
            }
        }
    }

}
