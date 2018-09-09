public class LC111 {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        int left = minDepth(root.left) + 1;
        int right = minDepth(root.right) + 1;
        if (root.left == null) return right;
        if (root.right == null) return left;
        return Math.min(left, right);
    }
}
