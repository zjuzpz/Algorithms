import java.util.*;
public class SummaryRanges {
    public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<String>();
        if(nums.length == 0) {return res;}
        StringBuffer cur = new StringBuffer();
        cur.append(nums[0]);
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] != nums[i - 1] + 1) {
                if(cur.charAt(cur.length() - 1) == '>') {
                    cur.append(nums[i - 1]);
                }
                res.add(cur.toString());
                cur = new StringBuffer();
                cur.append(nums[i]);
            } else if(cur.charAt(cur.length() - 1) != '>') {
                cur.append("->");
            }
        }
        if(cur.charAt(cur.length() - 1) == '>') {cur.append(nums[nums.length - 1]);}
        res.add(cur.toString());
        return res;
    }

}
