
public class MyPow {
    public static double myPow(double x, int n) {
        if(n == Integer.MIN_VALUE) {
            return 1 / (myPow(x, Integer.MAX_VALUE) * x);
        }
        if(n < 0) {return 1 / myPow(x, -n);}
        if(n == 0) {return 1;}
        if(n % 2 == 1) {
            return myPow(x * x, n / 2) * x;
        } else {
            return myPow(x * x, n / 2);
        }
    }
    
    public static double myPow2(double x, int n) {
        if(n == Integer.MIN_VALUE) {
            return 1 / (myPow(x, Integer.MAX_VALUE) * x);
        }
        if(n < 0) {return 1 / myPow2(x, -n);}
        double res = 1.0;
        while(n != 0) {
            if(n % 2 == 1) {
                res *= x;
            }
            x *= x;
            n /= 2;
        }
        return res;
    }

	public static void main(String[] args) {
		System.out.println(myPow2(1, -2147483648));

	}

}
