
public class ClimbingStairs {
	
    public int climbStairs(int n) {
        if(n == 0) {return 0;}
        if(n == 1) {return 1;}
        int first = 1;
        int second = 2;
        int third;
        for(int i = 2; i < n; i++) {
            third = first + second;
            first = second;
            second = third;
        }
        return second;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
