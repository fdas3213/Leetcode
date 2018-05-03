public class lastword58 {
    public static void main(String[] args){
        String s = "Hello World";
        String s1 = "a  ";
        String s2 = "b a ";
        System.out.println(lengthOfLastWord(s1));
        System.out.println(lengthOfLastWord(s));
        System.out.println(lengthOfLastWord(s2));
    }

    public static int lengthOfLastWord(String s) {
        if (s.length() == 0 || s == " ") return 0;
        int l = s.length();
        String out = "";

        for (int i = l - 1; i >= 0; i --){
            if (s.charAt(i) == ' ' && out.length() > 0) return out.length();
            else if(s.charAt(i) != ' ') out += s.charAt(i);
        }
        return out.length();
    }
}
