// LeetCode 3547. Maximum Sum of Edge Values in a Graph — Hard
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/
// Submission 2202833246 — Accepted, Java
class Solution {
    public long maxScore(int n, int[][] edges) {
        // My thinking: every node has degree at most 2 and the graph
        // is connected, so it is a path (n - 1 edges) or a cycle
        // (n edges). A big number earns most when it sits next to
        // other big numbers, so I lay the values out as the odds
        // increasing and then the evens decreasing — the largest
        // values end up side by side in the middle. For a cycle I
        // add the wrap-around edge between the two ends.
        int[] arr = new int[n];
        int idx = 0;
        for (int x = 1; x <= n; x += 2) arr[idx++] = x;
        for (int x = (n % 2 == 0 ? n : n - 1); x >= 2; x -= 2) arr[idx++] = x;
        long total = 0;
        for (int i = 0; i < n - 1; i++) total += (long)arr[i] * arr[i + 1];
        if (edges.length == n) total += (long)arr[n - 1] * arr[0];
        return total;
    }
}
