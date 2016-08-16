import java.util.*;
public class LargestRectangleInHistogram {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<Integer>();
        int res = 0;
        int curIndex;
        for(int i = 0; i < heights.length; i++) {
            while(stack.size() != 0 && heights[stack.get(stack.size() - 1)] > heights[i]) {
                curIndex = stack.pop();
                if(stack.size() != 0) {
                    res = Math.max(res, (i - stack.get(stack.size() - 1) - 1) * heights[curIndex]);
                } else {
                    res = Math.max(res, i * heights[curIndex]);
                }
            }
            stack.add(i);
        }
        int right = heights.length;
        while(stack.size() != 0) {
            curIndex = stack.pop();
            if(stack.size() != 0) {
                res = Math.max(res, (right - stack.get(stack.size() - 1) - 1) * heights[curIndex]);
            } else {
                res = Math.max(res, right * heights[curIndex]);
            }
        }
        return res;
    }
    
    public static void main(String[] args) {
    	int[] heights = {2, 1, 5, 6, 2, 3};
    	System.out.println(new LargestRectangleInHistogram().largestRectangleArea(heights));
    }

}
