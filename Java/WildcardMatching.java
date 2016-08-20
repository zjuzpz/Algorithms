
public class WildcardMatching {
    public boolean isMatch(String s, String p) {
        int scur = 0;
        int pcur = 0;
        int slast = 0;
        int plast = -1;
        while(scur < s.length()) {
            if(pcur < p.length() && (p.charAt(pcur) == s.charAt(scur) || p.charAt(pcur) == '?')) {
                pcur++;
                scur++;
            } else if(pcur < p.length() && p.charAt(pcur) == '*') {
                plast = pcur;
                slast = scur;
                pcur++;
            } else if(plast != -1) {
                slast++;
                scur = slast;
                pcur = plast + 1;
            } else {return false;}
        }
        while(pcur < p.length() && p.charAt(pcur) == '*') {pcur++;}
        return pcur == p.length();
    }

}
