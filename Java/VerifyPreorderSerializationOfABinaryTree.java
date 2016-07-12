
public class VerifyPreorderSerializationOfABinaryTree {
    public static boolean isValidSerialization(String preorder) {
        int required = 1;
        String s[] = preorder.split(",");
        for(int i = 0; i < s.length; i++) {
            if(s[i].equals("#")) {
                required--;
                if(required < 0) {return false;}
            } else {
                if(required == 0) {return false;}
                required++;
            }
        }
        return required == 0;
    }
    
    public static void main(String[] args) {
    	System.out.println(isValidSerialization("9,#,2,#,#"));
    }

}
