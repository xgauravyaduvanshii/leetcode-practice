// LeetCode 1962. Remove Stones to Minimize the Total — Medium
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/
// Submission 2204260892 — Accepted, C#

// My thinking: each operation should hit the biggest pile, because
// removing floor(pile / 2) stones from it takes away the most stones
// possible in one move, and making a big pile smaller never hurts a
// later move. A max-heap always hands me the biggest pile: I pop it,
// cut it down to pile minus pile / 2, and push it back. After k
// operations the heap holds the final piles, and their sum is the
// answer. .NET's PriorityQueue is a min-heap, so I store each pile
// with the negated pile as its priority to get max-heap behaviour.
public class Solution {
    public int MinStoneSum(int[] piles, int k) {
        var heap = new PriorityQueue<int, int>();
        foreach (int p in piles) {
            heap.Enqueue(p, -p);
        }
        for (int i = 0; i < k; i++) {
            int biggest = heap.Dequeue();
            biggest -= biggest / 2;
            heap.Enqueue(biggest, -biggest);
        }
        int total = 0;
        while (heap.Count > 0) {
            total += heap.Dequeue();
        }
        return total;
    }
}
