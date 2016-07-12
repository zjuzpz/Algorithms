
public class ReverseLinkedListII {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if(head == null) {return null;}
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode cur = dummy;
        for(int i = 1; i < m; i++) {
            cur = cur.next;
        }
        ListNode first = cur.next;
        ListNode second = first.next;
        ListNode third;
        for(int i = m; i < n; i++) {
            third = second.next;
            second.next = first;
            first = second;
            second = third;
        }
        cur.next.next = second;
        cur.next = first;
        return dummy.next;
    }

}
