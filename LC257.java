import java.util.ArrayList;
import java.util.List;

public class LC257 {
    public static List<String> binaryTreePaths(TreeNode root){
        List<String> out = new ArrayList<>();
        helper(root, out, "");
        return out;
    }

    private static void helper(TreeNode root, List<String> list, String path){
        if (root == null) return;
        if (root.left == null && root.right == null) {
            list.add(path + root.val);
            return;
        }
        path = path + root.val + "->";
        helper(root.left, list, path);
        helper(root.right, list, path);
    }

    public static void main(String[] args){
        TreeNode n = new TreeNode(1);
        n.left = new TreeNode(2);
        n.right = new TreeNode(3);
        n.left.right = new TreeNode(5);
        System.out.println(binaryTreePaths(n));
    }
}
