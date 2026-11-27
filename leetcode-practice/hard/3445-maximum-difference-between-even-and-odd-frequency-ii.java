// LeetCode 3445. Maximum Difference Between Even and Odd Frequency II — Hard
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/
// Submission 2202541319 — Accepted 693/693, Java
class Solution {
    public int maxDifference(String s, int k) {
        // My thinking: only the two digits a and b matter, so I try all
        // 20 pairs. For one pair, a substring's value is the difference
        // of the prefix counts (count_a - count_b), so I keep, for each
        // parity of the two counts, the smallest prefix difference seen
        // at a start that is far enough back: at least k behind, and no
        // later than the last b, so b appears at least twice in the
        // substring. The best end minus that minimum is the answer.
        int n = s.length();
        final int INF = 1000000000;
        int ans = -INF;
        for (char a = '0'; a <= '4'; a++) {
            for (char b = '0'; b <= '4'; b++) {
                if (a == b) continue;
                int[] pa = new int[n + 1];
                int[] pb = new int[n + 1];
                for (int i = 0; i < n; i++) {
                    pa[i + 1] = pa[i] + (s.charAt(i) == a ? 1 : 0);
                    pb[i + 1] = pb[i] + (s.charAt(i) == b ? 1 : 0);
                }
                int[][] best = new int[2][2];
                for (int i = 0; i < 2; i++) {
                    for (int j = 0; j < 2; j++) best[i][j] = INF;
                }
                int lastB = -1;
                int added = -1;  // highest start index added so far
                for (int r = 0; r <= n; r++) {
                    int bound = Math.min(r - k, lastB);
                    while (added < bound) {
                        added++;
                        int d = pa[added] - pb[added];
                        int x = pa[added] & 1, y = pb[added] & 1;
                        if (d < best[x][y]) best[x][y] = d;
                    }
                    int cur = best[1 - (pa[r] & 1)][pb[r] & 1];
                    if (cur < INF) {
                        ans = Math.max(ans, (pa[r] - pb[r]) - cur);
                    }
                    if (r < n && s.charAt(r) == b) lastB = r;
                }
            }
        }
        return ans;
    }
}
