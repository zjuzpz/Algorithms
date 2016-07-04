import java.util.*;
public class GroupAnagram {

	
    public static List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<List<String>>();
        Map<String, ArrayList<String>> lookup = new HashMap<String, ArrayList<String>>();
        char[] tem;
        String sorted;
        for(String s:strs) {
            tem = s.toCharArray();
            Arrays.sort(tem);
            sorted = new String(tem);
            if(!lookup.containsKey(sorted)) {
                lookup.put(sorted, new ArrayList<String>());
            }
            lookup.get(sorted).add(s);
        }
        for(ArrayList<String> value:lookup.values()) {
            res.add(value);
        }
        return res;
    }
    
	public static void main(String[] args) {
		String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
		System.out.println(groupAnagrams(strs));

	}

}
