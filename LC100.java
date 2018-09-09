public class LC100 {
    public static boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null || q == null) return false;
        if (p == null && q == null) return true;
        if (p.val == q.val){
            return isSameTree(p.left, q.left) && isSameTree(p.right,q.right);
        }
        return false;
    }
}
