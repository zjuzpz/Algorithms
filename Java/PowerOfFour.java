
public class PowerOfFour {
    public boolean isPowerOfFour(int num) {
        if(num <= 0 || num == 2) {return false;}
        if(num == 1) {return true;}
        return (num & (num - 1)) == 0 && (num & (0x55555555)) == num;
    }

}
