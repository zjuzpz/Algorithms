
public class ConvertSortedListToBinarySearchTree {
    public TreeNode sortedListToBST(ListNode head) {
        if(head == null) {return null;}
        return buildTree(head);
    }
    
    private TreeNode buildTree(ListNode node) {
        ListNode dummy = new ListNode(-1);
        dummy.next = node;
        ListNode fast = node;
        ListNode slow = node;
        ListNode prev = dummy;
        while(fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            prev = prev.next;
        }
        TreeNode root = new TreeNode(slow.val);
        prev.next = null;
        if(dummy.next != null) {
            root.left = buildTree(dummy.next);
        }
        if(slow.next != null) {
            root.right = buildTree(slow.next);
        }
        return root;
    }

}
