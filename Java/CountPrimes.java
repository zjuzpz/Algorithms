
public class CountPrimes {
    public int countPrimes(int n) {
        if(n < 2) {return 0;}
        boolean[] isNotPrime = new boolean[n];
        int res = 0;
        int cur;
        for(int i = 2; i < n; i++) {
            if(!isNotPrime[i]) {
                res++;
                cur = i + i;
                while(cur < n) {
                    isNotPrime[cur] = true;
                    cur += i;
                }
            }
        }
        return res;
    }

}
