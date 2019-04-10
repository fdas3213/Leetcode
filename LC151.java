public class LC151 {
    public static String reverseWords(String s) {
        StringBuilder out = new StringBuilder();
        StringBuilder sb = new StringBuilder();
        for (int i = s.length()-1; i>=0; i--){
            if (s.charAt(i) == ' ' && sb.toString().length() == 0) continue;
            else if (s.charAt(i) == ' ' && sb.toString().length() > 0){
                out.append(sb.reverse().toString());
                out.append(' ');
                sb = new StringBuilder();
            }else{
                sb.append(s.charAt(i));
            }
        }
        out.append(sb.reverse().toString());
        return out.toString().trim();
    }

    public static void main(String[] args){
        String s1 = "the sky is blue";
        String s2 = "  hello world!  ";
        String s3 = "a good   example";
        System.out.println(reverseWords(s1));
        System.out.println(reverseWords(s2));
        System.out.println(reverseWords(s3));
    }
}
