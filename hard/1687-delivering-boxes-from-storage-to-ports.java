// LeetCode 1687. Delivering Boxes from Storage to Ports — Hard
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/
// Submission 2201092889 — Accepted, Java
//
// My thinking: a trip carries boxes in order, so the
// split points are all that matter — I keep the cheapest
// cost to reach each split with a sliding window that
// respects the weight limit and a queue that always
// hands me the best split inside it.

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int boxDelivering(int[][] boxes, int portsCount, int maxBoxes, int maxWeight) {
        int n = boxes.length;
        int[] pref = new int[n];
        for (int i = 1; i < n; i++) {
            pref[i] = pref[i - 1] + (boxes[i][0] != boxes[i - 1][0] ? 1 : 0);
        }
        int[] dp = new int[n + 1];
        int[] wsum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            wsum[i + 1] = wsum[i] + boxes[i][1];
        }
        Deque<Integer> q = new ArrayDeque<>();
        q.addLast(0);
        int left = 0;
        for (int i = 1; i <= n; i++) {
            while (i - left > maxBoxes || wsum[i] - wsum[left] > maxWeight) {
                if (q.peekFirst() == left) {
                    q.pollFirst();
                }
                left++;
            }
            dp[i] = dp[q.peekFirst()] + pref[i - 1] - pref[q.peekFirst()] + 2;
            if (i < n) {
                while (!q.isEmpty() && dp[q.peekLast()] - pref[q.peekLast()] >= dp[i] - pref[i]) {
                    q.pollLast();
                }
                q.addLast(i);
            }
        }
        return dp[n];
    }
}
