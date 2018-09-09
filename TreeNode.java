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

    public static void inorder(TreeNode n){
        if (n.left != null) inorder(n.left);
        System.out.println(n.val);
        if (n.right != null) inorder(n.right);
    }

    public static void preorder(TreeNode n){
        System.out.println(n.val);
        if (n.left != null) preorder(n.left);
        if (n.right != null) preorder(n.right);
    }

    public static void postorder(TreeNode n){
        if (n.left != null) postorder(n.left);
        if (n.right != null) postorder(n.right);
        System.out.println(n.val);
    }


    public static void main(String[] args){
        TreeNode t = new TreeNode(3);
        t.left = new TreeNode(9);
        t.right = new TreeNode(20);
        t.right.left = new TreeNode(15);
        t.right.right = new TreeNode(7);
        //TreeNode.toString(t);
        System.out.println("Inorder");
        TreeNode.inorder(t);
        System.out.println("Preorder");
        TreeNode.preorder(t);
        System.out.println("Postorder");
        TreeNode.postorder(t);
    }
}
