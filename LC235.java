public class LC235 {
    public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root.val < p.val && root.val < q.val) {
            return lowestCommonAncestor(root.right, p, q);
        }else if (root.val > p.val && root.val > q.val){
            return lowestCommonAncestor(root.left, p,q);
        }else{
            return root;
        }
    }

    public static void main(String[] args){
        //test cases
        TreeNode t = new TreeNode(6);
        t.left = new TreeNode(2);
        t.right = new TreeNode(8);
        t.left.left = new TreeNode(0);
        t.left.right = new TreeNode(4);
        TreeNode result = lowestCommonAncestor(t, new TreeNode(2), new TreeNode(8));
        System.out.println(result.val);
        TreeNode result2 = lowestCommonAncestor(t, new TreeNode(2), new TreeNode(4));
        System.out.println(result2.val);
    }
}
