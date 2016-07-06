
public class ReverseString {
    public static String reverseString(String s) {
        char[] charArray = s.toCharArray();
        char tem;
        int i = 0;
        int j = charArray.length - 1;
        while(i < j) {
            tem = charArray[i];
            charArray[i] = charArray[j];
            charArray[j] = tem;
            i++;
            j--;
        }
        return new String(charArray);
    }
    
    public static String reverseString2(String s) {
    	StringBuffer sb = new StringBuffer(s);
    	sb.reverse();
    	return sb.toString();
    }

	public static void main(String[] args) {
		System.out.println(reverseString("hello world"));

	}

}
