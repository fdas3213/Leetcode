public class strStr28 {

    public static void main(String[] args){
        System.out.println(strStr("hello","ll"));
        System.out.println(strStr("aaaaa","bba"));
        System.out.println(strStr("mississippi", "issip"));


    }


    public static int strStr(String haystack, String needle){
        int l1 = haystack.length(), l2 = needle.length();
        if (l1 < l2){
            return -1;
        }else if(l2 == 0){
            return 0;
        }

        for (int i = 0; i < l1; i ++){
            if (haystack.charAt(i) == needle.charAt(0)){
                String match = "";
                int k = i;
                while (match.length() < l2 && k < l1){
                    match += haystack.charAt(k++);
                }
                if (match.equals(needle)) return i;
            }
        }

        return -1;
    }
}
