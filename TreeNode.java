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

    public static String traverse(TreeNode n){
        StringBuilder s = new StringBuilder();
        s.append(n.val);
        System.out.println(n.val);
        if (n.left != null) traverse(n.left);
        if (n.right != null) traverse(n.right);
        return s.toString();
    }

    public static void main(String[] args){
        TreeNode t = new TreeNode(5);
        t.left = new TreeNode(7);
        t.right = new TreeNode(10);
        //TreeNode.toString(t);
        System.out.println(traverse(t));
    }
}
