public class LC110 {
    public static boolean isBalanced(TreeNode root) {
        if (root == null || (root.left == null && root.right == null)) return true;
        int left = depth(root.left);
        int right = depth(root.right);
        return Math.abs(left-right) <= 1 && isBalanced(root.left) && isBalanced(root.right);
    }

    private static int depth(TreeNode node){
        if (node == null) return 0;
        int left = depth(node.left) + 1;
        int right = depth(node.right) + 1;
        return Math.max(left, right);
    }
}
