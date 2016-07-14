import java.util.*;
public class DifferentWaysToAddParentheses {
    public List<Integer> diffWaysToCompute(String input) {
        if(input.length() == 0) {return null;}
        List<Integer> nums = new ArrayList<Integer>();
        List<Character> opter = new ArrayList<Character>();
        int tem = 0;
        for(int i = 0; i < input.length(); i++) {
            if(input.charAt(i) >= '0' && input.charAt(i) <= '9') {
                tem = tem * 10 + input.charAt(i) - '0';
            } else {
                nums.add(tem);
                opter.add(input.charAt(i));
                tem = 0;
            }
        }
        nums.add(tem);
        return recur(nums, opter);
    }
    
    private List<Integer> recur(List<Integer> nums, List<Character> opter) {
        if(nums.size() <= 1) {return nums;}
        List<Integer> res = new ArrayList<Integer>();
        List<Integer> left;
        List<Integer> right;
        for(int i = 0; i < opter.size(); i++) {
            left = new ArrayList<Integer>(recur(nums.subList(0, i + 1), opter.subList(0, i)));
            right = new ArrayList<Integer>(recur(nums.subList(i + 1, nums.size()), opter.subList(i + 1, opter.size())));
            for(int l : left) {
                for(int r : right) {
                    res.add(calculate(l, r, opter.get(i)));
                }
            }
        }
        return res;
    }
    
    private int calculate(int l, int r, Character opter) {
        if(opter == '+') {return l + r;}
        if(opter == '-') {return l - r;}
        return l * r;
    }

}
