public class LC58 {

    public static int lengthOfLastWord(String s) {
        if (s.length() == 0 || s == " ") return 0;
        int l = s.length();
        int k = 0;

        for (int i = l - 1; i >= 0; i --){
            if (s.charAt(i) == ' ' && k > 0) return k;
            else if(s.charAt(i) != ' ') k++;
        }
        return k;
    }

    public static int lengthOfLastWordSolution2(String s){
        int l = s.length();
        if (l == 0 || s.equals(" ")) return 0;
        int lastwordl = 0;
        int i = 0;
        while(i < l){
            int out = 0;
            if(s.charAt(i) != ' '){
                for (int j = i; j< l && s.charAt(j) != ' '; j++){
                    out++;
                }
                lastwordl = out;
            }else out++;
            i += out;
        }
        return lastwordl;
    }

    public static void main(String[] args){
        String s1 = "Hello World";
        System.out.println(lengthOfLastWord(s1));
        String s2 = "a";
        System.out.println(lengthOfLastWord(s2));
        String s3 = " a";
        System.out.println(lengthOfLastWord(s3));
        String s4 = "a ";
        System.out.println(lengthOfLastWord(s3));
    }

}
