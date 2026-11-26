// LeetCode 4114. Count Consistent Subarrays II — Hard
// https://leetcode.com/problems/count-consistent-subarrays-ii/
// Submission 2203741357 — Accepted, C#

public class Solution {
    public long CountConsistent(int[] nums) {
        // My thinking: a subarray is consistent when its
        // bitwise AND equals its minimum. The AND of a
        // subarray is always <= every element, so it is
        // <= the minimum, and equality holds exactly when
        // the AND value itself occurs in the subarray.
        // For each right endpoint r, keep the distinct
        // ANDs of all subarrays ending at r (at most ~20
        // of them, since each AND step can only clear
        // bits) together with how many starts give each
        // AND. A subarray ending at r with AND x is
        // consistent exactly when its start is at or
        // before the most recent occurrence of x, so for
        // each AND group we count the starts in its
        // range that lie at or before that last
        // occurrence. Summing over all r counts every
        // consistent subarray once.
        long ans = 0;
        var cur = new List<(int a, int c)>();
        var last = new Dictionary<int, int>();
        for (int r = 0; r < nums.Length; r++) {
            int v = nums[r];
            var nxt = new List<(int a, int c)>();
            nxt.Add((v, 1));
            foreach (var (a, c) in cur) {
                int na = a & v;
                if (na == nxt[nxt.Count - 1].a) {
                    var t = nxt[nxt.Count - 1];
                    nxt[nxt.Count - 1] = (t.a, t.c + c);
                } else {
                    nxt.Add((na, c));
                }
            }
            cur = nxt;
            last[v] = r;
            int end = r;
            foreach (var (a, c) in cur) {
                int s = end - c + 1;
                if (last.TryGetValue(a, out int lp) && lp >= s) {
                    ans += Math.Min(end, lp) - s + 1;
                }
                end = s - 1;
            }
        }
        return ans;
    }
}
