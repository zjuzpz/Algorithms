
public class MultiplyStrings {
    public String multiply(String num1, String num2) {
        if(num1.equals("0") || num2.equals("0")) {return "0";}
        int[] nums = new int[num1.length() + num2.length()];
        for(int i = 0; i < num1.length(); i++) {
            for(int j = 0; j < num2.length(); j++) {
                nums[i + j + 1] += Integer.parseInt("" + num1.charAt(i)) * Integer.parseInt("" + num2.charAt(j));
            }
        }
        int carry = 0;
        int tem;
        for(int i = nums.length - 1; i >= 0; i--) {
            tem = nums[i] + carry;
            nums[i] = tem % 10;
            carry = tem / 10;
        }
        StringBuffer res = new StringBuffer();
        int i = 0;
        while(i < nums.length) {
            if(nums[i] == 0) {
                i++;
            } else {
                break;
            }
        }
        for(; i < nums.length; i++) {
            res.append(nums[i]);
        }
        return res.toString();
    }

}
