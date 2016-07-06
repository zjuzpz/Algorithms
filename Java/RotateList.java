
public class RotateList {

    public ListNode rotateRight(ListNode head, int k) {
        if(head == null) {return null;}
        int length = 1;
        ListNode cur = head;
        while(cur.next != null) {
            length++;
            cur = cur.next;
        }
        cur.next = head;
        k %= length;
        int j = length - k;
        ListNode newHead;
        for(int i = 0; i < j; i++) {
            cur = cur.next;
        }
        newHead = cur.next;
        cur.next = null;
        return newHead;
    }
}
