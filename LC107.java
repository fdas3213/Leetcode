import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
import java.util.Queue;

public class LC107 {
    public static List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> out = new LinkedList<>();
        if (root == null) return out;
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> inner = new ArrayList<>();
            for (int i = 0; i < size; i++){
                if(queue.peek().left != null) queue.offer(queue.peek().left);
                if(queue.peek().right != null) queue.offer(queue.peek().right);
                inner.add(queue.poll().val);
            }
            out.add(0,inner);
        }
        return out;
    }
}
