import java.util.Arrays;

public class anagram242 {
    //use selection sort
    public static boolean isAnagram(String s, String t){
        if(s.length() != t.length()) return false;

        char[] arrS = s.toCharArray();
        char[] arrT = t.toCharArray();

        for (int i = 0; i < arrS.length; i++){
            char s_smallest = arrS[i];
            char t_smmalest = arrT[i];
            int s_idx = i;
            int t_idx = i;

            for (int j = i+1; j< arrS.length; j++){
                if (arrS[j]-s_smallest < 0) {
                    s_smallest = arrS[j];
                    s_idx = j;
                }
                if (arrT[j] - t_smmalest < 0){
                    t_smmalest = arrT[j];
                    t_idx = j;
                }
            }
            char s_tmp = arrS[i];
            arrS[i] = s_smallest;
            arrS[s_idx] = s_tmp;

            char t_tmp = arrT[i];
            arrT[i] = t_smmalest;
            arrT[t_idx] = t_tmp;
        }

        return Arrays.equals(arrS,arrT);
    }


    public static void main(String[] args){
        System.out.println(isAnagram("anagram","nagaram"));
        System.out.println(isAnagram("rat","car"));


    }

}
