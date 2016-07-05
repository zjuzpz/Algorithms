
public class GasStation {

    public static int canCompleteCircuit(int[] gas, int[] cost) {
        int[] diff = new int[gas.length];
        int total = 0;
        for(int i = 0; i < gas.length; i++) {
            diff[i] = gas[i] - cost[i];
            total += diff[i];
        }
        if(total < 0) {return -1;}
        total = 0;
        int res = 0;
        for(int i = 0; i < diff.length; i++) {
            total += diff[i];
            if(total < 0) {
                total = 0;
                res = i + 1;
            }
        }
        return res;
    }
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
