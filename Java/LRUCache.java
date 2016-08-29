import java.util.*;

class ListNode {
    int val;
    ListNode prev;
    ListNode next;
    int key;
    
    ListNode(int val) {
        this.val = val;
    }
}

class DoubleLinkedList {
    ListNode head;
    ListNode tail;
    
    public void add(ListNode node) {
        if(head == null) {
            head = node;
            tail = node;
        } else {
            tail.next = node;
            node.prev = tail;
            tail = tail.next;
        }
    }
    
    public void delete(ListNode node) {
        if(node == head) {
            if(head == tail) {
                head = null;
                tail = null;
            } else {
                node.next.prev = null;
                head = node.next;
                node.next = null;
            }
        } else if(node == tail) {
            node.prev.next = null;
            tail = node.prev;
            node.prev = null;
        } else {
            node.prev.next = node.next;
            node.next.prev = node.prev;
            node.next = null;
            node.prev = null;
        }
    }
}

public class LRUCache {
    
    int cap = 0;
    int curCap = 0;
    Map<Integer, ListNode> lookup = new HashMap<Integer, ListNode>();
    DoubleLinkedList list;
    
    public LRUCache(int capacity) {
        this.cap = capacity;
        this.list = new DoubleLinkedList();
    }
    
    public int get(int key) {
        if(!lookup.containsKey(key)) {
            return -1;
        }
        ListNode node = lookup.get(key);
        list.delete(node);
        list.add(node);
        return node.val;
    }
    
    public void set(int key, int value) {
        ListNode node;
        if(lookup.containsKey(key)) {
            node = lookup.get(key);
            node.val = value;
            list.delete(node);
            list.add(node);
        } else {
            if(cap == curCap) {
                node = list.head;
                list.delete(node);
                lookup.remove(node.key);
                curCap--;
            }
            node = new ListNode(value);
            node.key = key;
            lookup.put(key, node);
            list.add(node);
            curCap++;
        }
    }
}










import java.util.*;
public class LRUCache {
    
    LinkedHashMap<Integer, Integer> map;
    
    public LRUCache(int capacity) {
    	final int cap = capacity;
        map = new LinkedHashMap<Integer, Integer>(capacity) {
            protected boolean removeEldestEntry(Map.Entry eldest) {
                return size() > cap;
            }
        };
    }
    
    public int get(int key) {
        if(map.containsKey(key)) {
            this.set(key, map.get(key));
            return map.get(key);
        }
        return -1;
    }
    
    public void set(int key, int value) {
        if(map.containsKey(key)) {
            map.remove(key);
        }
        map.put(key, value);
    }
}
