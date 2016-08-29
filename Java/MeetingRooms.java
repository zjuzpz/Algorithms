import java.util.Arrays;
import java.util.Comparator;

class Interval {
	int start;
	int end;
	Interval(int s, int e) {
		start = s;
		end = e;
	}
}

public class MeetingRooms {
	
	public static boolean canAttendMeetings(Interval[] intervals) {
		if(intervals == null || intervals.length == 0) {return true;}
		Arrays.sort(intervals, new Comparator<Interval>() {
			public int compare(Interval a, Interval b) {
				return a.start - b.start;
			} 
		});
		for(int i = 1; i < intervals.length; i++) {
			if(intervals[i].start < intervals[i - 1].end) {
				return false;
			}
		}
		return true;
	}

}
