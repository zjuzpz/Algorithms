import java.util.Arrays;


public class RotateImage {
	
    public static void rotate(int[][] matrix) {
        int n = matrix.length;
        int times = n / 2;
        int tem;
        for(int i = 0; i < times; i++) {
            for(int j = i; j < n - 1 - i; j++) {
                tem = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - j][i];
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                matrix[j][n - 1 - i] = tem;
            }
        }
    }

	public static void main(String[] args) {
		int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
		rotate(matrix);
		for(int i = 0; i < matrix.length; i++) {
			System.out.println(Arrays.toString(matrix[i]));
		}

	}

}
