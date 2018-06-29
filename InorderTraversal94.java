import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class InorderTraversal94 {
    public static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> l = new ArrayList<>();
        if (root.left != null) {
            inorderTraversal(root.left);
        }
        l.add(root.val);
        if (root.right != null) {
            inorderTraversal(root.right);
        }
        return l;
    }

    public static void main(String[] args){
        TreeNode n = new TreeNode(1);
        n.right = new TreeNode(2);
        n.right.left = new TreeNode(3);

        System.out.println(inorderTraversal(n));
    }
}
