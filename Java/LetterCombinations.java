import java.util.*;
public class letterCombinations {
	
	private static final Map<Character, String> lookup = new HashMap<Character, String>() {
        {
            put('2', "abc");
            put('3', "def");
            put('4', "ghi");
            put('5', "jkl");
            put('6', "mno");
            put('7', "pqrs");
            put('8', "tuv");
            put('9', "wxyz");
        }
    };  
            
	public static List<String> letterCombinations(String digits) {
	    List<String> res = new ArrayList<String>();
	    StringBuffer cur = new StringBuffer();
	    if(digits.length() != 0) {
	        String tem = lookup.get(digits.charAt(0));
	        for(int i = 0; i < tem.length(); i++) {
	            cur.append(tem.charAt(i));
	            recur(res, cur, 1, digits);
	            cur.deleteCharAt(cur.length() - 1);
	        }
	    }
	    return res;
	}
	
	public static void recur(List<String> res, StringBuffer cur, int start, String digits) {
	    if(start >= digits.length()) {
	        res.add(cur.toString());
	    } else {
	        String tem = lookup.get(digits.charAt(start));
	        for(int i = 0; i < tem.length(); i++) {
	            cur.append(tem.charAt(i));
	            recur(res, cur, start + 1, digits);
	            cur.deleteCharAt(cur.length() - 1);
	        }
	    }
	}

	public static void main(String[] args) {
		String digits = "23";
		List<String> res = letterCombinations(digits);
		System.out.println(res);

	}

}
