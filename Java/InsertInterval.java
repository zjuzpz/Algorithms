import java.util.*;
class Interval {
	int start;
	int end;
	Interval(int s, int e) {start = s; end = e;}
}
public class InsertInterval {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> res = new ArrayList<Interval>();
        for(int i = 0; i < intervals.size(); i++) {
            if(intervals.get(i).start > newInterval.end) {
                res.add(newInterval);
                for(int j = i; j < intervals.size(); j++) {
                    res.add(intervals.get(j));
                }
                return res;
            }
            if(intervals.get(i).end < newInterval.start) {
                res.add(intervals.get(i));
            } else {
                newInterval.start = Math.min(newInterval.start, intervals.get(i).start);
                newInterval.end = Math.max(newInterval.end, intervals.get(i).end);
            }
        }
        res.add(newInterval);
        return res;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
