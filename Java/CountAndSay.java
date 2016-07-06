import java.util.*;
public class CountAndSay {
    public static String countAndSay(int n) {
        List<String> prev = new ArrayList<String>();
        List<String> cur = new ArrayList<String>();
        prev.add("1");
        String curString;
        int curCount;
        for(int i = 1; i < n; i++) {
            curString = prev.get(0);
            curCount = 1;
            for(int j = 1; j < prev.size(); j++) {
                if(prev.get(j).equals(curString)) {
                    curCount++;
                } else {
                    cur.add(Integer.toString(curCount));
                    cur.add(curString);
                    curCount = 1;
                    curString = prev.get(j);
                }
            }
            cur.add(Integer.toString(curCount));
            cur.add(curString);
            prev = new ArrayList<String>(cur);
            cur.clear();
        }
        return String.join("", prev);
    }

	public static void main(String[] args) {
		System.out.print(countAndSay(4));

	}

}
