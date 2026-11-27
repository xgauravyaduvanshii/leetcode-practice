// LeetCode 2305. Fair Distribution of Cookies — Medium
// https://leetcode.com/problems/fair-distribution-of-cookies/
// Submission 2204665716 — Accepted, C#
//
// My thinking: same idea as the Python version — depth-first search over
// handing the bags out, biggest first, skipping children whose load
// duplicates one already tried and pruning any branch whose biggest load
// already reaches the best answer.
public class Solution {
    private int best;
    private int[] cookies;
    private int k;
    private int[] loads;

    public int DistributeCookies(int[] cookies, int k) {
        Array.Sort(cookies);
        Array.Reverse(cookies);
        this.cookies = cookies;
        this.k = k;
        loads = new int[k];
        best = 0;
        foreach (int c in cookies) best += c;
        Dfs(0);
        return best;
    }

    private void Dfs(int i) {
        if (i == cookies.Length) {
            int mx = 0;
            foreach (int x in loads) mx = Math.Max(mx, x);
            best = Math.Min(best, mx);
            return;
        }
        var seen = new HashSet<int>();
        for (int j = 0; j < k; j++) {
            if (seen.Contains(loads[j])) continue;
            seen.Add(loads[j]);
            loads[j] += cookies[i];
            int mx = 0;
            foreach (int x in loads) mx = Math.Max(mx, x);
            if (mx < best) Dfs(i + 1);
            loads[j] -= cookies[i];
            if (loads[j] == 0) break;
        }
    }
}
