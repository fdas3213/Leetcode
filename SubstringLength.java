public class SubstringLength {

    public static int lengthoflongestsubstring(String s){
        if (s == "") return 0;
        int l = 0;
        String out = "";
        int maxlength = 0;
        while (l < s.length()){
            char c = s.charAt(l);
            int char_idx = out.indexOf(c);
            if (char_idx == -1){
                out += c;
            }else{
                out = out.substring(char_idx+1) + c;
            }
            if (out.length() > maxlength){
                maxlength = out.length();
            }
            //System.out.println("Now the String is: " + out);
            //System.out.println("Now the length is: " + maxlength);
            l ++;
        }
        return maxlength;
    }

    public static void main(String[] args){

        String s1 = "abcabcbb";
        String s2 = "bbbbb";
        System.out.println(lengthoflongestsubstring(s1));
        System.out.println(lengthoflongestsubstring(s2));
        String s3 = "pwwkew";

        System.out.println(lengthoflongestsubstring(s3));
        //System.out.println("wke".indexOf("w"));
        //System.out.println("wke".substring(1) + "w");
    }
}
