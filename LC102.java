import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;

public class LC102 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> out = new ArrayList<>();
        if (root == null) return out;
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()){
            //add a level number
            int level = queue.size();
            List<Integer> subList = new ArrayList<>();
            for (int i = 0; i < level;i++){
                if(queue.peek().left != null) queue.offer(queue.peek().left);
                if(queue.peek().right != null) queue.offer(queue.peek().right);
                subList.add(queue.poll().val);
            }
            out.add(subList);
        }
        return out;
    }
}
