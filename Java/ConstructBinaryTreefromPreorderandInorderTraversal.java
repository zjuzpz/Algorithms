import java.util.*;

public class ConstructBinaryTreefromPreorderandInorderTraversal {
	
    public static TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> lookup = new HashMap<Integer, Integer>();
        int inStart = 0;
        int preStart = 0;
        int inEnd = inorder.length - 1;
        for(int i = 0; i < inorder.length; i++) {
            lookup.put(inorder[i], i);
        }
        return helper(lookup, preorder, inStart, inEnd, preStart);
    }
    
    public static TreeNode helper(Map<Integer, Integer> lookup, int[] preorder, int inStart, int inEnd, int preStart) {
        if(inStart > inEnd) {return null;}
        TreeNode node = new TreeNode(preorder[preStart]);
        int position = lookup.get(preorder[preStart]);
        TreeNode left = helper(lookup, preorder, inStart, position - 1, preStart + 1);
        TreeNode right = helper(lookup, preorder, position + 1, inEnd, preStart + position - inStart + 1);
        node.left = left;
        node.right = right;
        return node;
    }

	public static void main(String[] args) {
		int[] preorder = {3, 1, 2, 5, 4};
		int[] inorder = {1, 2, 3, 4, 5};
		TreeNode root = buildTree(preorder, inorder);
		System.out.println(root.val);
		System.out.println(root.left.val);
		System.out.println(root.left.right.val);
		System.out.println(root.right.val);
		System.out.println(root.right.left.val);
	}

}
