public class LC171 {

    public static int titleToNumber(String s) {
        int num = 0, l = s.length() -1;
        for(int i = 0; i< s.length();i++){
            int cur = (int)Math.pow(26,l) * (s.charAt(i)-'A'+1);
            num += cur;
            l --;
        }
        return num;
    }

    public static int titleToNumberShort(String s){
        int num = 0;
        for (int i =0; i < s.length(); i++){
            num = num*26 + (s.charAt(i) -'A'+1);
        }
        return num;
    }


    public static void main(String[] args){
        System.out.println(titleToNumber("A"));
        System.out.println(titleToNumber("AB"));
        System.out.println(titleToNumber("ZY"));
    }
}
