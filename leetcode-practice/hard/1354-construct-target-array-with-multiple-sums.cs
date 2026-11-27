public class Solution {
    public bool IsPossible(int[] target) {
        // My thinking: run the process backwards — the biggest
        // number was the last one built, so take away the sum
        // of the rest (in one jump with a remainder) until
        // everything is back down to 1.
        long total = 0;
        var heap = new PriorityQueue<int, int>();
        foreach (int x in target) {
            total += x;
            heap.Enqueue(x, -x);
        }
        while (heap.Peek() > 1) {
            int biggest = heap.Dequeue();
            long rest = total - biggest;
            if (rest == 0 || biggest <= rest) return false;
            long newVal = biggest % rest;
            if (newVal == 0) newVal = rest;
            total = rest + newVal;
            heap.Enqueue((int)newVal, -(int)newVal);
        }
        return true;
    }
}
