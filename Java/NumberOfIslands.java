
public class NumberOfIslands {
    public int numIslands(char[][] grid) {
        if(grid.length == 0) {return 0;}
        int res = 0;
        boolean [][] visited = new boolean[grid.length][grid[0].length];
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == '1' && !visited[i][j]) {
                    res++;
                    visited[i][j] = true;
                    DFS(grid, visited, i, j);
                }
            }
        }
        return res;
    }
    
    public void DFS(char[][] grid, boolean [][] visited, int x, int y) {
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for(int[] direction: directions) {
            int i = x + direction[0];
            int j = y + direction[1];
            if(i >= 0 && i < grid.length && j >= 0 && j < grid[0].length && grid[i][j] == '1' && !visited[i][j]) {
                visited[i][j] = true;
                DFS(grid, visited, i, j);
            }
        }
    }

}
