import java.util.*;
public class SubstringWithConcatenationOfAllWords {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<Integer>();
        Map<String, Integer> lookup = new HashMap<String, Integer>();
        String word;
        if(words.length == 0) {return res;}
        int wordLength = words[0].length();
        if(words.length * wordLength < s.length()) {return res;}
        for(int i = 0; i < words.length; i++) {
            if(!lookup.containsKey(words[i])) {
                lookup.put(words[i], 0);
            }
            lookup.replace(words[i], lookup.get(words[i]) + 1);
        }
        int cur = 1;
        int total = words.length;
        for(int i = 0; i < s.length() - words.length * wordLength + 1; i++) {
            word = s.substring(i, i + wordLength);
            if(lookup.containsKey(word)) {
                lookup.replace(word, lookup.get(word) - 1);
                if(recur(lookup, s, i + wordLength, wordLength, cur, total)) {
                    res.add(i);
                }
                lookup.replace(word, lookup.get(word) + 1);
            }
        }
        return res;
    }
    
    private boolean recur(Map<String, Integer> lookup, String s, int start, int wordLength, int cur, int total) {
        if(cur == total) {return true;}
        if(start + wordLength > s.length()) {return false;}
        String word = s.substring(start, start + wordLength);
        if(lookup.containsKey(word)) {
            int count = lookup.get(word);
            if(count == 0) {return false;}
            lookup.replace(word, count - 1);
            if(recur(lookup, s, start + wordLength, wordLength, cur + 1, total)) {
                lookup.replace(word, count + 1);
                return true;
            }
            lookup.replace(word, count + 1);
        }
        return false;
    }
}
