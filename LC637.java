import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class LC637 {
    public static List<Double> averageOfLevels(TreeNode root) {
        List<Double> out = new ArrayList<>();
        if (root == null) return out;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()){
            double sum = 0, level = queue.size();
            for (int i =0; i < level;i++){
                TreeNode cur = queue.poll();
                if(cur.left != null) queue.offer(cur.left);
                if(cur.right != null) queue.offer(cur.right);
                sum += cur.val;
            }
            out.add(sum/level);
        }
        return out;
    }
}
