
public class Sqrtx {
    public int mySqrt(int x) {
        int lower = 1;
        int upper = x;
        int mid;
        while(lower < upper) {
            mid = (lower + upper) / 2;
            if(x / mid == mid) {return mid;}
            if(x / mid < mid) {
                upper = mid - 1;
            } else {
                lower = mid + 1;
            }
        }
        if(upper * upper > x) {return upper - 1;}
        return upper;
    }

}
