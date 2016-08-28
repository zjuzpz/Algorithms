import java.util.*;
public class WordBreakII {
    public List<String> wordBreak(String s, Set<String> wordDict) {
        List<String> res = new ArrayList<String>();
        if(!hasSentences(s, wordDict)) {return res;}
        StringBuffer cur = new StringBuffer();
        recur(res, cur, wordDict, s, 0);
        return res;
    }
    
    private boolean hasSentences(String s, Set<String> wordDict) {
        if(s == null || s.length() == 0) {return false;}
        boolean[] dp = new boolean[s.length()];
        String word;
        for(int i = 0; i < s.length(); i++) {
            word = s.substring(0, i + 1);
            if(wordDict.contains(word)) {
                dp[i] = true;
            } else {
                for(int j = 0; j < i; j++) {
                    if(dp[j] && wordDict.contains(s.substring(j + 1, i + 1))) {
                        dp[i] = true;
                    }
                }
            }
        }
        return dp[dp.length - 1];
    }
    
    private void recur(List<String> res, StringBuffer cur, Set<String> wordDict, String s, int start) {
        String word;
        StringBuffer next;
        if(start == s.length()) {
            res.add(cur.toString());
        } else {
            for(int i = start; i < s.length(); i++) {
                word = s.substring(start, i + 1);
                if(wordDict.contains(word)) {
                    next = new StringBuffer(cur);
                    if(next.length() != 0) {
                        next.append(' ');
                    }
                    next.append(word);
                    recur(res, next, wordDict, s, i + 1);
                }
            }
        }
    }

}
