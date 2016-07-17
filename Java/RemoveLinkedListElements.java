
public class RemoveLinkedListElements {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(-1);
        ListNode prev = dummy;
        ListNode cur = head;
        while(cur != null) {
            if(cur.val != val) {
                prev.next = cur;
                prev = cur;
            }
            cur = cur.next;
        }
        prev.next = null;
        return dummy.next;
    }

}
