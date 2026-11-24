// LeetCode 3320. Count The Number of Winning Sequences — Hard
// https://leetcode.com/problems/count-the-number-of-winning-sequences/
// Submission 2202367614 — Accepted, Java
//
// My thinking: Bob's move in each round is F, W or E, never the same twice
// in a row, and Alice's move is fixed. I track the score difference (Bob's
// points minus Alice's) with a DP over rounds, keyed by Bob's last move and
// the running difference, which ranges from -n to n. A move gains +1 if it
// beats Alice's creature, -1 if Alice's beats it, 0 on a tie (F beats E, W
// beats F, E beats W). The answer is the number of sequences ending with a
// difference greater than 0.
class Solution {
    private static final int MOD = 1_000_000_007;

    public int countWinningSequences(String s) {
        // 0 = F, 1 = W, 2 = E; beats[b] is the creature b beats.
        int[] beats = {2, 0, 1};
        int n = s.length();
        int[] alice = new int[n];
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            alice[i] = c == 'F' ? 0 : (c == 'W' ? 1 : 2);
        }
        int width = 2 * n + 1;
        long[][] dp = new long[3][width];
        for (int b = 0; b < 3; b++) {
            dp[b][gain(b, alice[0], beats) + n] = 1;
        }
        for (int i = 1; i < n; i++) {
            long[][] ndp = new long[3][width];
            for (int last = 0; last < 3; last++) {
                for (int d = 0; d < width; d++) {
                    long v = dp[last][d];
                    if (v == 0) {
                        continue;
                    }
                    for (int b = 0; b < 3; b++) {
                        if (b == last) {
                            continue;
                        }
                        int nd = d + gain(b, alice[i], beats);
                        ndp[b][nd] = (ndp[b][nd] + v) % MOD;
                    }
                }
            }
            dp = ndp;
        }
        long ans = 0;
        for (int last = 0; last < 3; last++) {
            for (int d = n + 1; d < width; d++) {
                ans = (ans + dp[last][d]) % MOD;
            }
        }
        return (int) ans;
    }

    private int gain(int b, int a, int[] beats) {
        if (beats[b] == a) {
            return 1;
        }
        if (beats[a] == b) {
            return -1;
        }
        return 0;
    }
}
