public class LC5 {
    public static String longestPalindrome(String s) {
        if (s.length() <= 1) return s;
        int n = s.length(), start = 0, max = 0;

        boolean[][] dp = new boolean[n][n];

        for(int i =n-1; i>=0; i--){
            for(int j = i;j<n;j++){
                /*dp[i][j] is true only if front and end characters match &&
                the characters between them are palindrome or distance btw
                front and end is less than 3
                 */
                dp[i][j] = (s.charAt(i) == s.charAt(j)) &&
                        (j-i < 3||
                        dp[i+1][j-1]);
                if(dp[i][j] && j-i+1 > max){
                    max = j-i+1;
                    start = i;
                }
            }
        }
        return s.substring(start, start+max);
    }

    public static void main(String[] args){
        String s1 = "babad";
        String s2 = "cbba";
        System.out.println(longestPalindrome(s1));
        System.out.println(longestPalindrome(s2));
    }
}
