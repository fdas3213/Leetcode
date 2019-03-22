import java.util.Arrays;
import java.util.HashMap;
import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

public class LC501 {
    public static int[] findMode(TreeNode root){
        if(root == null) return new int[0];
        HashMap<Integer, Integer> hm = new HashMap<>();
        List<Integer> store = new ArrayList<>();
        Stack<TreeNode> st = new Stack<>();
        int max = 0;
        //first pass is to traverse the tree and get count for each value
        while(!st.empty() || root != null){
            while(root != null){
                st.push(root);
                root = root.left;
            }
            root = st.pop();
            if(!hm.containsKey(root.val)) hm.put(root.val,0);
            int count = hm.get(root.val) + 1;
            if (count >= max) max = count;
            hm.put(root.val, count);
            root = root.right;
        }
        //second pass is to find values whose count = max_count
        for(int key: hm.keySet()){
            if(hm.get(key) == max) store.add(key);
        }
        int[] out = new int[store.size()];
        for(int i = 0; i < out.length;i++) out[i] = store.get(i);
        return out;
    }

    public static void main(String[] args){
        TreeNode t = new TreeNode(1);
        t.right = new TreeNode(2);
        t.right.left = new TreeNode(2);
        System.out.println(Arrays.toString(findMode(t)));

        TreeNode t1 = new TreeNode(1);
        t1.right = new TreeNode(2);
        System.out.println(Arrays.toString(findMode(t1)));
    }
}
