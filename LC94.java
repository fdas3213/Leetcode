import java.util.List;
import java.util.ArrayList;
import java.util.Stack;

public class LC94 {
    private static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode cur = root;

        while(cur != null || !stack.empty()){
            while(cur != null){
                stack.add(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            out.add(cur.val);
            cur = cur.right;
        }
        return out;
    }
    public static void main(String[] args){
        TreeNode t1 = new TreeNode(1);
        t1.right = new TreeNode(2);
        t1.right.left = new TreeNode(3);
        System.out.println(inorderTraversal(t1));
    }
}

