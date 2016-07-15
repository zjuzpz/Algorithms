import java.util.*;
public class PascalsTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(numRows <= 0) {return res;}
        List<Integer> cur = new ArrayList<Integer>();
        cur.add(1);
        res.add(cur);
        for(int i = 1; i < numRows; i++) {
            cur = new ArrayList<Integer>();
            cur.add(1);
            for(int j = 0; j < i - 1; j++) {
                cur.add(res.get(res.size() - 1).get(j) + res.get(res.size() - 1).get(j + 1));
            }
            cur.add(1);
            res.add(cur);
        }
        return res;
    }

}
