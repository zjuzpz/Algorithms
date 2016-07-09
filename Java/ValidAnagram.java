import java.util.*;
public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {return false;}
        Map<Character, Integer> lookup = new HashMap<Character, Integer>();
        for(int i = 0; i < s.length(); i++) {
            if(!lookup.containsKey(s.charAt(i))) {
                lookup.put(s.charAt(i), 0);
            }
            lookup.put(s.charAt(i), lookup.get(s.charAt(i)) + 1);
        }
        for(int i = 0; i < t.length(); i++) {
            if(!lookup.containsKey(t.charAt(i)) || lookup.get(t.charAt(i)) == 0) {return false;}
            lookup.put(t.charAt(i), lookup.get(t.charAt(i)) - 1);
        }
        return true;
    }
    
    public boolean isAnagram2(String s, String t) {
        if(s.length() != t.length()) {return false;}
        int[] lookup = new int['z' - 'a' + 1];
        for(int i = 0; i < s.length(); i++) {
            lookup[s.charAt(i) - 'a']++;
        }
        for(int i = 0; i < t.length(); i++) {
            lookup[t.charAt(i) - 'a']--;
            if(lookup[t.charAt(i) - 'a'] < 0) {return false;}
        }
        return true;
    }
    
    public static void main(String[] args) {
    	System.out.println(new ValidAnagram().isAnagram2("a", "b"));
    }

}
