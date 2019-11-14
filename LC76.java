public class LC76 {
    public static String minWindow(String s, String t){
        //sanity check
        if (t == null || s.length() < t.length()) return null;
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        //initialize an array of size 256
        int[] hash = new int[256];

        /* for char in t, increment its value */
        for (char c : tArr) hash[c]++;

        /* initialize left, count, and max */
        int left = 0, count = tArr.length, max = Integer.MAX_VALUE;
        String output = "";

        for (int right = 0; right < sArr.length; right++){
            /* decrement the value of each character in s */
            hash[sArr[right]] --;

            /* if the value >= 0, then it means the char is also in t, so it's a valid char */
            if (hash[sArr[right]] >= 0){
                count--;
            }
            /* If a valid substring is found, start minimizing it */
            while (left < right && hash[sArr[left]] < 0){
                hash[sArr[left]]++;
                left ++;
            }

            if (count == 0 && max > right-left+1){
                max = right-left+1;
                output = s.substring(left, right+1);
            }
        }
        return output;
    }

    public static void main(String[] args){
        String s = "ADOBECODEBANC";
        String t = "ABC";
        System.out.println(minWindow(s,t));
    }
}
