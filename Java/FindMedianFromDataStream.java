import java.util.*;


public class FindMedianFromDataStream {
    PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
    PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(new Comparator<Integer>(){
        public int compare(Integer a, Integer b) {
            return b - a;
        }
    });

    // Adds a number into the data structure.
    public void addNum(int num) {
        minHeap.add(num);
        if(minHeap.size() > maxHeap.size() + 1 || (maxHeap.size() != 0 && minHeap.peek() < maxHeap.peek())) {
            maxHeap.add(minHeap.poll());
        }
        if(minHeap.size() < maxHeap.size()) {
            minHeap.add(maxHeap.poll());
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        if(minHeap.size() == maxHeap.size()) {
            return (minHeap.peek() + maxHeap.peek()) / 2.0;
        } else {
            return (double)minHeap.peek();
        }
    }

}
