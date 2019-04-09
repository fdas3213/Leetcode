public class LC129 {
    public static int sumNumbers(TreeNode root) {
        return sum(root, 0);
    }

    private static int sum(TreeNode root, int total) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return total*10+root.val;
        return sum(root.left, total*10+root.val) + sum(root.right, total*10+root.val);
    }

    public static void main(String[] args){

    }
}

