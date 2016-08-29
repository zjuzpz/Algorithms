
public class ConvertSortedArrayToBinarySearchTree {
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums == null || nums.length == 0) {return null;}
        return build(nums, 0, nums.length - 1);
    }
    
    private TreeNode build(int[] nums, int lower, int upper) {
        if(lower > upper) {return null;}
        int mid = lower + (upper - lower) / 2;
        if((upper - lower) % 2 == 1) {mid++;}
        TreeNode node = new TreeNode(nums[mid]);
        node.left = build(nums, lower, mid - 1);
        node.right = build(nums, mid + 1, upper);
        return node;
    }

}
