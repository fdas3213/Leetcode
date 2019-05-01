import java.util.LinkedList;

public class LC129 {
    public static int sumNumbers(TreeNode root) {
        return sum(root, 0);
    }

    private static int sum(TreeNode root, int total) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return total*10+root.val;
        return sum(root.left, total*10+root.val) + sum(root.right, total*10+root.val);
    }

    public static int sol2(TreeNode root) {
        //another way using level order traversal
        if (root == null) return 0;
        if (root.left == null && root.right == null) return root.val;
        LinkedList<TreeNode> queue = new LinkedList<>();
        LinkedList<Integer> sum = new LinkedList<>();
        queue.offer(root);
        sum.offer(root.val);
        int total = 0;
        while (!queue.isEmpty()){
            TreeNode cur = queue.poll();
            int curSum = sum.poll();
            if (cur.left == null && cur.right == null) total += curSum;
            if (cur.left != null) {
                queue.offer(cur.left);
                sum.offer(curSum*10 + cur.left.val);
            }
            if (cur.right != null) {
                queue.offer(cur.right);
                sum.offer(cur.right.val + curSum*10);
            }
        }
        return total;
    }

    public static void main(String[] args){
        TreeNode n = new TreeNode(1);
        n.left = new TreeNode(2);
        n.right = new TreeNode(3);
        System.out.println(sumNumbers(n));
    }
}

