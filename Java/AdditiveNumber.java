
public class AdditiveNumber {
    public boolean isAdditiveNumber(String num) {
        double num1;
        double num2;
        for(int i = 0; i < num.length() / 2 + 1; i++) {
            for(int j = i + 1; j < num.length() / 3 * 2 + 1; j++) {
                if(j == num.length() - 1) {return false;}
                num1 = Double.parseDouble(num.substring(0, i + 1));
                num2 = Double.parseDouble(num.substring(i + 1, j + 1));
                if(recur(num, num1, num2, j + 1)) {return true;}
                if(num.charAt(i + 1) == '0') {break;}
            }
            if(num.charAt(0) == '0') {break;}
        }
        return false;
    }
    
    private boolean recur(String num, double num1, double num2, int start) {
        if(start == num.length()) {return true;}
        double sum = num1 + num2;
        double num3;
        for(int i = start; i < num.length(); i++) {
            num3 = Double.parseDouble(num.substring(start, i + 1));
            if(sum == num3) {return recur(num, num2, num3, i + 1);}
            if(sum < num3) {return false;}
            if(num.charAt(start) == '0') {break;}
        }
        return false;
    }

	public static void main(String[] args) {
		System.out.println(new AdditiveNumber().isAdditiveNumber("8917"));

	}

}
