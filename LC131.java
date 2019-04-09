import java.util.List;
import java.util.ArrayList;

public class LC131 {
    public static List<List<String>> partition(String s) {
        List<List<String>> out = new ArrayList<>();
        if (s == null) return out;
        backtracking(out, new ArrayList<>(), s, 0);
        return out;
    }

    private static void backtracking(List<List<String>> list, List<String> tempList, String s, int index){
        if(index == s.length()){
            list.add(new ArrayList<>(tempList));
        }
        for (int i = index; i < s.length(); i++){
            String inner = s.substring(index, i+1);
            if(isPalindrome(inner)){
                tempList.add(inner);
                backtracking(list, tempList, s, i+1);
                tempList.remove(tempList.size()-1);
            }
        }
    }

    private static boolean isPalindrome(String s){
        int start = 0, end = s.length()-1;
        while (start < end){
            if (s.charAt(start++) != s.charAt(end--)) return false;
        }
        return true;
    }

    public static void main(String[] args){
        System.out.println(partition("aab"));
    }
}
