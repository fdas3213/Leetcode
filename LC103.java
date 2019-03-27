import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;

public class LC103 {
    public static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> out = new ArrayList<>();
        if (root == null) return out;
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int direction = 1;
        while(!queue.isEmpty()){
            int level = queue.size();
            LinkedList<Integer> subList = new LinkedList<>();
            for(int i = 0; i < level; i++){
                TreeNode cur = queue.poll();
                if (direction % 2 == 0){
                    subList.addFirst(cur.val);
                }else{
                    subList.add(cur.val);
                }
                if (cur.left != null) queue.offer(cur.left);
                if (cur.right != null) queue.offer(cur.right);
            }
            out.add(subList);
            direction++;
        }
        return out;
    }

    public static void main(String[] args){
        TreeNode n = new TreeNode(1);
        n.left = new TreeNode(2);
        n.right = new TreeNode(3);
        n.left.left = new TreeNode(4);
        n.right.right = new TreeNode(5);
        System.out.println(zigzagLevelOrder(n));
    }
}

