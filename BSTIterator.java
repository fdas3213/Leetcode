import java.util.LinkedList;
import java.util.Queue;

public class BSTIterator {
    TreeNode n;
    Queue<TreeNode> queue;
    public BSTIterator(TreeNode root) {
        n = root;
        queue = new LinkedList<>();
        inorder(n);
    }

    private void inorder(TreeNode n){
        if (n == null) return;
        inorder(n.left);
        queue.offer(n);
        inorder(n.right);
    }

    /** @return the next smallest number */
    public int next() {
        return queue.poll().val;
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return queue.isEmpty();
    }

    public static void main(String[] args){
        TreeNode res = new TreeNode(7);
        res.left = new TreeNode(3);
        res.right = new TreeNode(15);
        res.right.left = new TreeNode(9);
        res.right.right = new TreeNode(20);
        BSTIterator obj = new BSTIterator(res);
        System.out.println(obj.next());
        System.out.println(obj.hasNext());
    }
}
