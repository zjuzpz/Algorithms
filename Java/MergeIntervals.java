import java.util.*;

public class MergeIntervals {
	
    public List<Interval> merge(List<Interval> intervals) {
        Collections.sort(intervals, new Comparator<Interval>() {
            public int compare(Interval l1, Interval l2) {
                return l1.start - l2.start;
            }
        });
        List<Interval> res = new ArrayList<Interval>();
        if(intervals.size() == 0) {return res;}
        Interval cur = intervals.get(0);
        Interval next;
        for(int i = 1; i < intervals.size(); i++) {
            next = intervals.get(i);
            if(next.start > cur.end) {
                res.add(cur);
                cur = next;
            } else {
                cur.end = Math.max(cur.end, next.end);
            }
        }
        res.add(cur);
        return res;
    }

	public static void main(String[] args) {
		List<Interval> intervals = new ArrayList<Interval>();
		intervals.add(new Interval(2, 6));
		intervals.add(new Interval(15, 18));
		intervals.add(new Interval(8, 10));
		intervals.add(new Interval(1, 3));
		System.out.println(new MergeIntervals().merge(intervals));

	}

}
