public class LC58 {

    public static int lengthOfLastWord(String s){
        int l = s.length();
        if (l == 0 || s.equals(" ")) return 0;
        int index = -1;
        for (int i = 0; i < l;i++){
            if(s.charAt(i) == ' ') index = i;
        }
        return s.length() - index -1;
    }

    public static void main(String[] args){
        String s1 = "Hello World";
        System.out.println(lengthOfLastWord(s1));
        String s2 = "a";
        System.out.println(lengthOfLastWord(s2));
    }

}
