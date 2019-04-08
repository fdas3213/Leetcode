import java.util.*;

public class LC127 {
    public static int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if(beginWord == endWord) return 1;
        Set<String> wordset = new HashSet<>(wordList);
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        int distance = 2;

        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                String cur = queue.poll();
                for (int j = 0; j < cur.length(); j++){
                    StringBuilder sb = new StringBuilder(cur);
                    for (char ch = 'a'; ch <= 'z'; ch++){
                        sb.setCharAt(j, ch);
                        String tmp = sb.toString();
                        if(wordset.contains(tmp)) {
                            if(tmp.equals(endWord)) return distance;
                            queue.offer(tmp);
                            wordset.remove(tmp);
                        }
                    }
                }
            }
            distance++;
        }
        return 0;
    }
    public static void main(String[] args){
        List<String> wList = new ArrayList<>();
        wList.add("hot");
        wList.add("dot");
        wList.add("dog");
        wList.add("lot");
        wList.add("log");
        wList.add("cog");
        System.out.println(ladderLength("hit","cog", wList));
    }
}
