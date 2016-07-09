import java.util.*;
public class Combinations {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(n < 1 || k < 0 || k > n) {return res;}
        List<Integer> cur = new ArrayList<Integer>();
        for(int i = 1; i <= n - k + 1; i++) {
            cur.add(i);
            recur(cur, res, i + 1, n, k);
            cur.remove(cur.size() - 1);
        }
        return res;
    }
    
    public void recur(List<Integer> cur, List<List<Integer>> res, int start, int end, int k) {
        if(cur.size() == k) {
            res.add(new ArrayList<Integer>(cur));
            return;
        }
        for(int i = start; i <= end - k + 1 + cur.size(); i++) {
            cur.add(i);
            recur(cur, res, i + 1, end, k);
            cur.remove(cur.size() - 1);
        }
    }

}
