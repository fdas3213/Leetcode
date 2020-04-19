import java.util.Deque;
import java.util.LinkedList;

public class LC71 {
    public static String simplifyPath(String path) {
        if(path.length() == 0) return path;
        Deque<String> st = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        for(String s : path.split("/")){
            if (s.equals("..")) st.poll();
            else if (!s.equals(".") && !s.equals("")) st.push(s);
        }
        while(!st.isEmpty()){
            sb.append("/").append(st.pollLast());
        }
        return sb.toString();
    }

    public static void main(String[] args){
        String s1 = "/home//foo";
        String s2 = "/a/./b/../../c/";
        System.out.println(simplifyPath(s1));
        System.out.println(simplifyPath(s2));
    }
}
