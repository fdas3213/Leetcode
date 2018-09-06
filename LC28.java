public class LC28 {
    public static int strStr(String haystack, String needle) {
        int l1 = haystack.length(), l2 = needle.length();
        if (l1 < l2) return -1;
        if (l2 == 0) return 0;
        for(int i = 0; i<=l1-l2; i++){
            if(haystack.substring(i,i+l2).equals(needle)) return i;
        }
        return -1;
    }

    public static void main(String[] args){
        String h1 = "hello";
        String n1 = "ll";
        System.out.println(strStr(h1,n1));
    }
}

