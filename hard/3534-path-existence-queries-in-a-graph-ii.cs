// LeetCode 3534. Path Existence Queries in a Graph II — Hard
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/
// Submission 2202814537 — Accepted, C#
public class Solution {
    public int[] PathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        // My thinking: two nodes are joined when their values differ
        // by at most maxDiff, so after sorting by value the graph
        // becomes a chain of intervals — a node reaches exactly the
        // nodes whose values lie within maxDiff of it. The cheapest
        // way across is to always jump to the farthest value still
        // within reach, and that greedy jump is a function on sorted
        // positions, so binary lifting counts how many jumps a query
        // needs. A gap wider than maxDiff between neighbours splits
        // the components, and then the answer is -1.
        int[] order = Enumerable.Range(0, n).OrderBy(i => nums[i]).ToArray();
        int[] vals = new int[n];
        int[] pos = new int[n];
        for (int p = 0; p < n; p++) { vals[p] = nums[order[p]]; pos[order[p]] = p; }
        int[] go = new int[n];
        int r = 0;
        for (int i = 0; i < n; i++) {
            if (r < i) r = i;
            while (r + 1 < n && vals[r + 1] - vals[i] <= maxDiff) r++;
            go[i] = r;
        }
        int[] comp = new int[n];
        int cid = 0;
        for (int i = 1; i < n; i++) {
            if (vals[i] - vals[i - 1] > maxDiff) cid++;
            comp[i] = cid;
        }
        const int LOG = 18;
        int[][] up = new int[LOG][];
        up[0] = (int[])go.Clone();
        for (int k = 1; k < LOG; k++) {
            up[k] = new int[n];
            for (int i = 0; i < n; i++) up[k][i] = up[k - 1][up[k - 1][i]];
        }
        int[] ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int pu = pos[queries[qi][0]], pv = pos[queries[qi][1]];
            if (pu == pv) { ans[qi] = 0; continue; }
            if (comp[pu] != comp[pv]) { ans[qi] = -1; continue; }
            if (pu > pv) { int tmp = pu; pu = pv; pv = tmp; }
            int cur = pu, t = 0;
            for (int kk = LOG - 1; kk >= 0; kk--) {
                if (up[kk][cur] < pv) { cur = up[kk][cur]; t += 1 << kk; }
            }
            ans[qi] = t + 1;
        }
        return ans;
    }
}
