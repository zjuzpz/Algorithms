import java.util.Arrays;


public class SpiralMatrixII {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int rounds = n / 2;
        boolean last = false;
        if(n % 2 == 1) {
        	rounds++;
        	last = true;
        }
        int cur = 1;
        for(int round = 0; round < rounds; round++) {
            for(int j = round; j < n - round - 1; j++) {
                matrix[round][j] = cur;
                cur++;
            }
            for(int i = round; i < n - round - 1; i++) {
                matrix[i][n - round - 1] = cur;
                cur++;
            }
            for(int j = n - round - 1; j > round; j--) {
                matrix[n - round - 1][j] = cur;
                cur++;
            }
            for(int i = n - round - 1; i > round; i--) {
                matrix[i][round] = cur;
                cur++;
            }
        }
        if(last) {matrix[n / 2][n / 2] = cur;}
        return matrix;
    }

	public static void main(String[] args) {
		int[][] matrix;
		int n = 2;
		matrix = new SpiralMatrixII().generateMatrix(n);
		for(int i = 0; i < n; i++) {
			System.out.println(Arrays.toString(matrix[i]));
		}

	}

}
