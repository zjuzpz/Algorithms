import java.util.*;

public class CountingBits {
    public int[] countBits(int num) {
        List<Integer> lookup = new ArrayList<Integer>();
        lookup.add(0);
        int cur = 0;
        int base = 1;
        for(int i = 0; i < num; i++) {
            if(cur == base) {
                cur = 0;
                base = lookup.size();
            }
            lookup.add(lookup.get(cur) + 1);
            cur++;
        }
        int[] res = new int[lookup.size()];
        for(int i = 0; i < lookup.size(); i++) {
            res[i] = lookup.get(i);
        }
        return res;
    }

}
