import java.util.Stack;

public class LC572 {
    public static boolean isSubtree(TreeNode s, TreeNode t){
        if (s == null || t == null) return false;
        Stack<TreeNode> st = new Stack<>();
        st.push(s);
        while(!st.empty()){
            TreeNode cur = st.pop();
            if(isSametree(cur, t)) return true;
            if (cur != null) {
                if (cur.right != null) st.push(cur.right);
                if(cur.left != null) st.push(cur.left);
            }
        }
        return false;
    }

    private static boolean isSametree(TreeNode p, TreeNode q){
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val == q.val) return isSametree(p.left,q.left) && isSametree(p.right, q.right);
        return false;
    }

    public static void main(String[] args){
        TreeNode s = new TreeNode(1);
        TreeNode t = new TreeNode(0);
        System.out.println(isSubtree(s,t));
    }
}
