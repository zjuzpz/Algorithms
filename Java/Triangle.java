import java.util.*;
public class Triangle {
    public int minimumTotal(List<List<Integer>> triangle) {
        if(triangle.size() == 0) {return 0;}
        List<Integer> prev = new ArrayList<Integer>(triangle.get(0));
        List<Integer> cur;
        for(int i = 1; i < triangle.size(); i++) {
            cur = new ArrayList<Integer>();
            cur.add(prev.get(0) + triangle.get(i).get(0));
            int j = 1;
            while(j < triangle.get(i).size() - 1){
                cur.add(Math.min(prev.get(j - 1), prev.get(j)) + triangle.get(i).get(j));
                j++;
            }
            cur.add(prev.get(j - 1) + triangle.get(i).get(j));
            prev = cur;
        }
        return Collections.min(prev);
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
