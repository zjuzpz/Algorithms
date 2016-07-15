import java.util.*;
public class FindKPairsWithSmallestSums {
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<int[]> q = new PriorityQueue<int[]>(new Comparator<int[]>(){
            public int compare(int[] a, int[] b) {
                return b[1] + b[0] - a[1] - a[0];
            }
        });
        int[] tem;
        for(int i = 0; i < nums1.length; i++) {
            for(int j = 0; j < nums2.length; j++) {
                tem = new int[] {nums1[i], nums2[j]};
                q.add(tem);
                if(q.size() > k) {q.poll();}
            }
        }
        return new ArrayList<int[]>(q);
    }

}
