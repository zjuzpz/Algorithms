import java.util.*;

//For infinite board
public class GameOfLife {
    public void gameOfLife(int[][] board) {
        int m = board.length;
        if(m == 0) {return;}
        int n = board[0].length;
        Map<String, Integer> count = new HashMap<String, Integer>();
        String key;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] == 1) {
                    for(int x = -1; x < 2; x++) {
                        for(int y = -1; y < 2; y++) {
                            if((i + x >= 0 && i + x < m && j + y >= 0 && j + y < n)) {
                                key = Integer.toString(i + x) + " " + Integer.toString(j + y);
                                if(!count.containsKey(key)) {
                                    count.put(key, 0);
                                }
                                if(x != 0 || y != 0) {
                                    count.put(key, count.get(key) + 1);
                                }
                            }
                        }
                    }
                }
            }
        }
        int index = 0;
        int x;
        int y;
        int live;
        for(String position: count.keySet()) {
            live = count.get(position);
            for(int i = 0; i < position.length(); i++) {
                if(position.charAt(i) == ' '){
                    index = i;
                }
            }
            x = Integer.parseInt(position.substring(0, index));
            y = Integer.parseInt(position.substring(index + 1));
            if(live == 3 || (live == 2 && board[x][y] == 1)) {
                board[x][y] = 1;
            } else {
                board[x][y] = 0;
            }
        }
    }

}
