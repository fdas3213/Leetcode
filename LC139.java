import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LC139 {
    public static boolean wordBreak(String s, List<String> wordDict) {
        boolean[] f = new boolean[s.length() + 1];
        f[0] = true;
        for(int i=1; i <= s.length(); i++){
            for(int j=0; j < i; j++){
                if(f[j] && wordDict.contains(s.substring(j, i))){
                    f[i] = true;
                    System.out.println("i: "+i+" j: "+j+ " " + Arrays.toString(f));
                    break;
                }
            }
        }
        return f[s.length()];
    }


    public static void main(String[] args){
        //unit test 1
        String s = "leetcode";
        List<String> l1 = new ArrayList<>();
        l1.add("leet");
        l1.add("code");
        System.out.println(wordBreak(s, l1));
        //unit test 2
        String s1 = "applepenapple";
        List<String> l2 = new ArrayList<>();
        l2.add("apple");
        l2.add("pen");
        System.out.println(wordBreak(s1, l2));

    }
}
