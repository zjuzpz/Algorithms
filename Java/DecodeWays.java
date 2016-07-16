
public class DecodeWays {
    public int numDecodings(String s) {
        if(s.length() == 0 || s.charAt(0) == '0') {return 0;}
        int[] res = new int[s.length() + 1];
        res[0] = 1;
        res[1] = 1;
        char tem;
        for(int i = 1; i < s.length(); i++) {
            tem = s.charAt(i);
            if(tem == '0') {
                if(s.charAt(i - 1) == '0' || s.charAt(i - 1) - '0' > 2) {return 0;}
                res[i + 1] = res[i - 1];
            } else if(tem - '0' <= 6) {
                if(s.charAt(i - 1) == '1' || s.charAt(i - 1) == '2') {
                    res[i + 1] = res[i] + res[i - 1];
                } else {
                    res[i + 1] = res[i];
                }
            } else {
                if(s.charAt(i - 1) == '1') {
                    res[i + 1] = res[i] + res[i - 1];
                } else {
                    res[i + 1] = res[i];
                }
            }
        }
        return res[res.length - 1];
    }

}
