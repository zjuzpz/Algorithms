import java.util.*;

public class MaximumProductOfWordLengths {
    public static int maxProduct(String[] words) {
        List<Set<Character>> lookup = new ArrayList<Set<Character>>();
        Set<Character> cur;
        int res = 0;
        boolean flag = true;
        for(String word: words) {
            cur = new HashSet<Character>();
            for(int i = 0; i < word.length(); i++) {
                cur.add(word.charAt(i));
            }
            lookup.add(cur);
        }
        for(int i = 0; i < words.length; i++) {
            for(int j = i + 1; j < words.length; j++) {
                if(words[i].length() * words[j].length() < res) {
                    continue;
                }
                for(Character c:lookup.get(j)) {
                    if(lookup.get(i).contains(c)) {
                        flag = false;
                        break;
                    }
                }
                if(flag) {res = words[i].length() * words[j].length();}
                flag = true;
            }
        }
        return res;
     }
    
    public static void main(String[] args) {
    	String[] strings = {"a","ab","abc","d","cd","bcd","abcd"};
    	System.out.println(maxProduct(strings));
    }

}
