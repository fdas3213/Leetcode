import java.util.ArrayList;
import java.util.List;

public class InorderTraversal94 {
    public static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> l = new ArrayList<>();
        return inorder(root,l);
    }

    private static List<Integer> inorder(TreeNode root, List<Integer> l){
        if (root.left != null) inorder(root.left, l);
        l.add(root.val);
        if (root.right != null) inorder(root.right, l);
        return l;
    }

    public static void main(String[] args){
        TreeNode n = new TreeNode(1);
        n.right = new TreeNode(2);
        n.right.left = new TreeNode(3);

        System.out.println(inorderTraversal(n));
    }
}
