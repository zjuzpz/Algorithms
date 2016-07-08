
public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        StringBuffer res = new StringBuffer();
        if(strs.length == 0) {
            return "";
        }
        for(int i = 0; i < strs[0].length(); i++) {
            res.append(strs[0].charAt(i));
        }
        for(int i = 1; i < strs.length; i++) {
            if(strs[i].length() < res.length()) {
                res.delete(strs[i].length(), res.length());
            }
            for(int j = 0; j < res.length(); j++) {
                if(strs[i].charAt(j)!= res.charAt(j)) {
                    res.delete(j, res.length());
                }
            }
        }
        return res.toString();
    }

	public static void main(String[] args) {


	}

}
