import java.util.ArrayList;
import java.util.List;

public class LC113 {
    public static List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> out = new ArrayList<>();
        if (root == null) return out;
        backtrack(out, new ArrayList<>(), root, sum);
        return out;

    }

    private static void backtrack(List<List<Integer>> list, List<Integer> tempList, TreeNode root, int sum){
        if (root == null) return;
        tempList.add(root.val);
        if (root.left == null && root.right == null && root.val == sum){
            list.add(new ArrayList<>(tempList));
            tempList.remove(tempList.size()-1);
            return;
        }else{
            backtrack(list, tempList, root.left, sum-root.val);
            backtrack(list, tempList, root.right, sum-root.val);
        }
        tempList.remove(tempList.size()-1);
    }

    public static void main(String[] args){
        TreeNode n = new TreeNode(5);
        n.left = new TreeNode(4);
        n.right = new TreeNode(8);
        n.left.left = new TreeNode(11);
        n.left.left.left = new TreeNode(7);
        n.left.left.right = new TreeNode(2);
        n.right.left = new TreeNode(13);
        n.right.right = new TreeNode(4);
        n.right.right.left = new TreeNode(5);
        n.right.right.right = new TreeNode(1);
        System.out.println(pathSum(n, 22));
    }

}
