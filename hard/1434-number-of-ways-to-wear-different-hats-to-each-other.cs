using System.Collections.Generic;

public class Solution {
    public int NumberWays(IList<IList<int>> hats) {
        // My thinking: give the hats out one by one — each hat
        // can go to any person who likes it and has none yet —
        // and a bitmask remembers who is already wearing one.
        const int MOD = 1000000007;
        int n = hats.Count;
        List<int>[] likes = new List<int>[41];
        for (int i = 0; i < 41; i++) likes[i] = new List<int>();
        for (int person = 0; person < n; person++) {
            foreach (int h in hats[person]) likes[h].Add(person);
        }
        int[] dp = new int[1 << n];
        dp[0] = 1;
        for (int h = 1; h <= 40; h++) {
            for (int mask = (1 << n) - 1; mask >= 0; mask--) {
                foreach (int person in likes[h]) {
                    if ((mask & (1 << person)) == 0) {
                        dp[mask | (1 << person)] = (dp[mask | (1 << person)] + dp[mask]) % MOD;
                    }
                }
            }
        }
        return dp[(1 << n) - 1];
    }
}
