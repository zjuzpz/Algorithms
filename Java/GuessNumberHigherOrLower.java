
public class GuessNumberHigherOrLower {
    public int guessNumber(int n) {
        int lower = 0;
        int upper = n;
        int mid;
        int res;
        while(lower <= upper) {
            mid = lower + (upper - lower) / 2;
            res = guess(mid);
            if(res == 0) {return mid;}
            if(res == -1) {
                upper = mid - 1;
            } else {
                lower = mid + 1;
            }
        }
        return lower;
    }

	private  int guess(int mid) {
		int num = 1702766719;
		if(mid == num) {return 0;}
		if(mid > num) {return -1;}
		return 1;
	}
	
	public static void main(String[] args) {
		//System.out.println(Integer.MAX_VALUE);
		System.out.println(new GuessNumberHigherOrLower().guessNumber(2126753390));
	}

}
