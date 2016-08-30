import java.util.*;
public class TextJustification {
    public static List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<String>();
        if(words == null) {return res;}
        if(words.length == 0 || maxWidth <= 0) {
            res.add("");
            return res;
        }
        StringBuffer cur = new StringBuffer();
        int start = 0;
        int count = 0;
        int totalSpace;
        int wordCount;
        int space;
        int residual;
        for(int i = 0; i < words.length; i++) {
            if(count + words[i].length() > maxWidth) {
                wordCount = i - start;
                if(wordCount == 1) {
                    cur.append(words[start]);
                    while(cur.length() < maxWidth) {
                        cur.append(' ');
                    }
                } else {
                    totalSpace = maxWidth - count + wordCount;
                    space = totalSpace / (wordCount - 1);
                    residual = totalSpace % (wordCount - 1);
                    for(int j = start; j < i - 1; j++) {
                        cur.append(words[j]);
                        for(int k = 0; k < space; k++) {
                            cur.append(' ');
                        }
                        if(residual > 0) {
                            cur.append(' ');
                            residual--;
                        }
                    }
                    cur.append(words[i - 1]);
                }
                res.add(cur.toString());
                cur.setLength(0);
                start = i;
                count = words[i].length() + 1;
            } else {
                count += words[i].length() + 1;
            }
        }
        if(start == words.length - 1) {
            cur.append(words[start]);
        } else {
            for(int i = start; i < words.length; i++) {
                cur.append(words[i]);
                cur.append(' ');
            }
        }
        while(cur.length() < maxWidth) {
            cur.append(' ');
        }
        res.add(cur.toString());
        return res;
    }

	public static void main(String[] args) {
		int maxWidth = 1;
		String[] words = new String[]{"a", "b", "c", "d", "e"}; 
		System.out.println(fullJustify(words, maxWidth));

	}

}
