import java.util.ArrayDeque;
import java.util.Deque;


public class ImplementStackUsingQueues {
    Deque<Integer> d = new ArrayDeque<Integer>();
    int last;
    // Push element x onto stack.
    public void push(int x) {
        d.addLast(x);
        last = x;
    }

    // Removes the element on top of the stack.
    public void pop() {
        for(int i = 0; i < d.size() - 1; i++) {
            push(d.pollFirst());
        }
        d.pollFirst();
    }

    // Get the top element.
    public int top() {
        return last;
    }

    // Return whether the stack is empty.
    public boolean empty() {
        return d.isEmpty();
    }

}
