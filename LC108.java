public class LC108 {
    public static TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) return null;
        return helper(nums, 0, nums.length-1);
    }

    private static TreeNode helper(int[] nums, int start, int end){
        if(start > end) return null;
        int mid = (start + end)/2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = helper(nums, start, mid-1);
        root.right = helper(nums, mid+1, end);
        return root;
    }

    public static void main(String[] args){
        int[] nums = {-10,-3,0,5,9};
        TreeNode n = sortedArrayToBST(nums);
        TreeNode.toString(n);
    }
}
