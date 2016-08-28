
public class CopyListWithRandomPointer {
    public RandomListNode copyRandomList(RandomListNode head) {
        if(head == null) {return head;}
        RandomListNode cur = head;
        RandomListNode newHead;
        RandomListNode tem;
        while(cur != null) {
            RandomListNode copy = new RandomListNode(cur.label);
            copy.next = cur.next;
            cur.next = copy;
            cur = cur.next.next;
        }
        cur = head;
        while(cur != null) {
            if(cur.random != null) {
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }
        cur = head;
        newHead = head.next;
        tem = newHead;
        while(cur != null) {
            cur.next = cur.next.next;
            if(tem.next != null) {
                tem.next = tem.next.next;
            }
            cur = cur.next;
            tem = tem.next;
        }
        return newHead;
    }


}
