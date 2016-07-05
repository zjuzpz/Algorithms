import java.util.*;
public class ValidParentheses {
    public static boolean isValid(String s) {
        Map<Character, Character> lookup = new HashMap<Character, Character>() {
            {
                put(')', '(');
                put(']', '[');
                put('}', '{');
            }
        };
        Character cur;
        Stack<Character> stack = new Stack<Character>();
        for(int i = 0; i < s.length(); i++) {
        	cur = s.charAt(i);
            if(!lookup.containsKey(cur)) {
                stack.push(cur);
            } else {
                if(stack.isEmpty() || lookup.get(cur) != stack.pop()) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

	public static void main(String[] args) {
		System.out.println(isValid("()[]{}"));

	}

}
