// LeetCode 4086. Minimum Interval Selection to Cover Target Intervals — Hard
// https://leetcode.com/problems/minimum-interval-selection-to-cover-target-intervals/
// Submission 2203704885 — Accepted, Java
import java.util.*;

class Solution {
    public int minSelection(int[][] availableIntervals, int[][] targetIntervals) {
        // My thinking: first merge the target intervals (sorted, so
        // overlapping or touching targets join into one segment to
        // cover), then cover each merged segment greedily from left
        // to right. At the leftmost uncovered point, push every
        // available interval that starts at or before it into a
        // max-heap keyed by right end, and always take the one that
        // reaches furthest — the classic minimum-interval-cover
        // greedy, which is optimal because any cover of the point
        // must use an interval starting at or before it, and the
        // furthest-reaching one can only help later segments. If
        // the heap is empty, the segment cannot be covered, so
        // return -1. If the best interval ends exactly at the point
        // while the segment extends further, it makes no progress,
        // so the segment is uncoverable and we return -1 as well.
        // Point-interval edge case: an available interval ending
        // exactly at the uncovered point still covers it when that
        // point is the segment's right end — e.g. available [2,2]
        // covers target [2,2], because the loop stops once reach
        // equals r, and the interval is counted once.
        Arrays.sort(targetIntervals, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        List<int[]> merged = new ArrayList<>();
        for (int[] t : targetIntervals) {
            if (!merged.isEmpty() && t[0] <= merged.get(merged.size() - 1)[1]) {
                merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], t[1]);
            } else {
                merged.add(new int[]{t[0], t[1]});
            }
        }
        Arrays.sort(availableIntervals, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        int i = 0;
        int n = availableIntervals.length;
        Integer reach = null;
        int count = 0;
        for (int[] seg : merged) {
            int l = seg[0], r = seg[1];
            int point = (reach == null || reach < l) ? l : reach;
            while (reach == null || reach < r) {
                while (i < n && availableIntervals[i][0] <= point) {
                    heap.offer(availableIntervals[i][1]);
                    i++;
                }
                if (heap.isEmpty()) return -1;
                int best = heap.poll();
                if (best < point) return -1;
                if (best == point && point < r) return -1;
                reach = best;
                count++;
                point = reach;
            }
        }
        return count;
    }
}
