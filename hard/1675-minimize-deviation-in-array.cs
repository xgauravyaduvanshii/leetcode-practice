using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumDeviation(int[] nums) {
        // My thinking: first double every odd number so all
        // are even — then keep halving the biggest one while
        // it stays even and watch the spread shrink.
        var heap = new PriorityQueue<int, int>();
        int curMin = int.MaxValue;
        foreach (int x0 in nums) {
            int x = x0 % 2 == 1 ? x0 * 2 : x0;
            heap.Enqueue(x, -x);
            curMin = Math.Min(curMin, x);
        }
        int best = heap.Peek() - curMin;
        while (heap.Peek() % 2 == 0) {
            int x = heap.Dequeue() / 2;
            curMin = Math.Min(curMin, x);
            heap.Enqueue(x, -x);
            best = Math.Min(best, heap.Peek() - curMin);
        }
        return best;
    }
}
