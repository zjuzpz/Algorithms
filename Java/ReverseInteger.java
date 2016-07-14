
public class ReverseInteger {
    public int reverse(int x) {
        if(x < 0) {
            if(x == Integer.MIN_VALUE) {return 0;}
            return -reverse(-x);
        }
        double res = 0;
        while(x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        if(res < Integer.MIN_VALUE || res > Integer.MAX_VALUE) {return 0;}
        return (int)res;
    }

}
