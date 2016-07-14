
public class IntersectionOfTwoLinkedLists {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null) {return null;}
        int lengthA = 1;
        int lengthB = 1;
        ListNode curA = headA;
        ListNode curB = headB;
        while(curA.next != null) {
            curA = curA.next;
            lengthA++;
        }
        while(curB.next != null) {
            curB = curB.next;
            lengthB++;
        }
        if(curA != curB) {return null;}
        curA = headA;
        curB = headB;
        while(lengthA > lengthB) {
            curA = curA.next;
            lengthA--;
        }
        while(lengthB > lengthA) {
            curB = curB.next;
            lengthB--;
        }
        while(curA != curB) {
            curA = curA.next;
            curB = curB.next;
        }
        return curA;
    }

}
