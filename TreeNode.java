public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }

    public static void toString(TreeNode n){
        System.out.println(" " + n.val + " ");
        if (n.left != null) toString(n.left);
        if (n.right != null) toString(n.right);
    }
}
