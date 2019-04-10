import java.util.List;
import java.util.ArrayList;
import java.util.Stack;

public class LC144 {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        preorder(root, out);
        return out;
}

    private static void preorder(TreeNode root, List<Integer> l){
        //recursive way
        l.add(root.val);
        if(root.left != null) preorder(root.left, l);
        if(root.right != null) preorder(root.right, l);
    }

    public List<Integer> preorderIterative(TreeNode root) {
        //iterative way
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Stack<TreeNode> st = new Stack<>();
        st.push(root);
        while(!st.empty()){
            TreeNode cur = st.pop();
            if(cur != null){
                out.add(cur.val);
                if(cur.right != null) st.push(cur.right);
                if(cur.left != null) st.push(cur.left);
            }
        }
        return out;
    }
}
