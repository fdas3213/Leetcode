import java.util.Stack;

public class LC98 {
    public static boolean isValidBST(TreeNode root) {
        if(root ==  null) return true;
        Stack<TreeNode> st = new Stack<>();
        TreeNode pre = null;
        while(!st.empty() || root != null){
            while(root != null) {
                st.push(root);
                root = root.left;
            }
            root = st.pop();
            if(pre != null && root.val <= pre.val) return false;
            pre = root;
            root = root.right;
        }
        return true;
    }

    public static void main(String[] args){
        TreeNode t = new TreeNode(5);
        t.left = new TreeNode(1);
        t.right = new TreeNode(4);
        t.right.left = new TreeNode(3);
        t.right.right = new TreeNode(6);

        System.out.println(isValidBST(t));
    }
}
