public class LC112 {
    public static boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) return false;
        else{
            if (root.left == null && root.right == null) {
                if(root.val == sum) return true;
                else return false;
            }
            return hasPathSum(root.left, sum -root.val) || hasPathSum(root.right,sum-root.val);
        }
    }
}
