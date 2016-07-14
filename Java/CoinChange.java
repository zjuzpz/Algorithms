import java.util.*;
public class CoinChange {
    public int coinChange(int[] coins, int amount) {
        if(amount == 0) {return 0;}
        Arrays.sort(coins);
        Set<Integer> cur = new HashSet<Integer>();
        Set<Integer> next;
        Set<Integer> visited = new HashSet<Integer>();
        int res = 1;
        for(int coin: coins) {
            if(coin == amount) {
                return res;
            }
            if(coin < amount) {
                cur.add(coin);
                visited.add(coin);
            } else {
                break;
            }
        }
        while(cur.size() != 0) {
            next = new HashSet();
            for(int num : cur) {
                for(int coin : coins) {
                    if(num + coin == amount) {
                        return res + 1;
                    } else if(num + coin < amount) {
                        if(!visited.contains(num + coin)) {
                            next.add(num + coin);
                            visited.add(num + coin);
                        }
                    } else {
                        break;
                    }
                }
            }
            cur = next;
            res++;
        }
        return -1;
    }

}
