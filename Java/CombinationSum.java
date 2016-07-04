import java.util.*;

public class CombinationSum {
	
    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();
        if(candidates.length != 0) {
            recur(res, cur, target, candidates, 1);
            cur.add(candidates[0]);
            recur(res, cur, target - candidates[0], candidates, 0);
            cur.remove(cur.size() - 1);
        }
        return res;
    }
    
    public static void recur(List<List<Integer>> res, List<Integer> cur, int target, int[] candidates, int start) {
        if(target < 0 || start >= candidates.length) { return; }
        if(target == 0) {
            res.add(new ArrayList<Integer>(cur));
            return;
        }
        recur(res, cur, target, candidates, start + 1);
        cur.add(candidates[start]);
        recur(res, cur, target - candidates[start], candidates, start);
        cur.remove(cur.size() - 1);
    }
	
    public static void main(String[] args) {
		int[] candidates = {2, 3, 6, 7};
		System.out.println(combinationSum(candidates, 7));

	}

}
