import java.util.*;

public class GenerateParentheses {

    public static List<String> generateParenthesis(int n) {
        int left = 0;
        int right = 0;
        StringBuffer cur = new StringBuffer();
        List<String> res = new ArrayList<String>();
        if(n != 0) {
            recur(res, cur, left, right, n);
        }
        return res;
    }
    
    public static void recur(List<String> res, StringBuffer cur, int left, int right, int n) {
        if(left == right && left == n) {
            res.add(cur.toString());
            return;
        }
        if(left > right) {
            cur.append(")");
            recur(res, cur, left, right + 1, n);
            cur.deleteCharAt(cur.length() - 1);
        } 
        if(left < n) {
            cur.append("(");
            recur(res, cur, left + 1, right, n);
            cur.deleteCharAt(cur.length() - 1);
        }
    }
    
	public static void main(String[] args) {
		System.out.println(generateParenthesis(4));

	}

}
