import java.util.Stack;


public class ImplementQueueUsingStacks {
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();
    
    // Push element x to the back of queue.
    public void push(int x) {
        stack1.push(x);
    }

    // Removes the element from in front of queue.
    public void pop() {
        if(stack2.size() == 0) {
            stack1ToStack2();
        }
        stack2.pop();
    }

    // Get the front element.
    public int peek() {
        if(stack2.size() == 0) {
            stack1ToStack2();
        }
        return stack2.peek();
    }
    
    private void stack1ToStack2() {
        while(stack1.size() != 0) {
            stack2.push(stack1.pop());
        }
    }

    // Return whether the queue is empty.
    public boolean empty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }

}
