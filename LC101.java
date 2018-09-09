
public class LC101 {
    public static boolean isSymmetric(TreeNode root) {
        return (root == null) || isSymmetric(root.left, root.right);
    }

    private static boolean isSymmetric(TreeNode l, TreeNode r){
        if (l == null && r == null) return true;
        if (l == null || r == null) return false;
        return (l.val==r.val) && isSymmetric(l.left, r.right) && isSymmetric(l.right, r.left);
    }

    public static void main(String[] args){
        //unit test
        TreeNode t = new TreeNode(1);
        t.left = new TreeNode(2);
        t.right = new TreeNode(2);
        t.left.left = new TreeNode(3);
        t.left.right = new TreeNode(4);
        t.right.left = new TreeNode(4);
        t.right.right = new TreeNode(3);

        System.out.println(isSymmetric(t));
    }
}
