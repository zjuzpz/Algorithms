
public class AddDigits {
    public int addDigits(int num) {
        int res = num;
        int cur = 0;
        while(res >= 10) {
            while(res > 0) {
                cur += res % 10;
                res /= 10;
            }
            res = cur;
            cur = 0;
        }
        return res;
    }
    
    public int addDigits2(int num) {
        if(num == 0) {return 0;}
        if(num % 9 == 0) {return 9;}
        return num % 9;
    }

}
