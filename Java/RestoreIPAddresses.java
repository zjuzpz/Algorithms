import java.util.*;
public class RestoreIPAddresses {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<String>();
        if(s.length() == 0) {return res;}
        List<String> cur = new ArrayList<String>();
        recur(res, cur, s, 0);
        return res;
    }
    
    private void recur(List<String> res, List<String> cur, String s, int start) {
        if(start >= s.length()) {
            if(cur.size() == 4) {
                res.add(String.join(".", cur));
            }
            return;
        }
        if(cur.size() == 4) {return;}
        if(s.charAt(start) == '0') {
            cur.add("0");
            recur(res, cur, s, start + 1);
            cur.remove(cur.size() - 1);
            return;
        }
        int tem = 0;
        for(int i = start; i < s.length(); i++) {
            tem = tem * 10 + s.charAt(i) - '0';
            if(tem <= 255) {
                cur.add(Integer.toString(tem));
                recur(res, cur, s, i + 1);
                cur.remove(cur.size() - 1);
            } else {
                break;
            }
        }
    }

	public static void main(String[] args) {
		String s = "12345";
		Character c;
		int a = 0;
		for(int i = 0; i < s.length(); i++) {
			c = s.charAt(i);
			a = a * 10 + s.charAt(i) - '0';
		}
		System.out.println(a);
		System.out.println(new RestoreIPAddresses().restoreIpAddresses("25525511135"));
		System.out.println(new RestoreIPAddresses().restoreIpAddresses("010010"));

	}

}
