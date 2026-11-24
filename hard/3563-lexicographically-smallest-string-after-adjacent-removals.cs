// LeetCode 3563. Lexicographically Smallest String After Adjacent Removals — Hard
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/
// Submission 2202849401 — Accepted, C#
using System;

public class Solution {
    public string LexicographicallySmallestString(string s) {
        // My thinking: I work on intervals. can[i][j] says whether
        // s[i..j] can vanish completely — either it splits into two
        // vanishing halves, or its first character pairs with some
        // later consecutive character after the middle vanishes.
        // dp[i][j] is the smallest string obtainable from s[i..j]:
        // either keep s[i] and reduce the rest, or delete s[i]
        // together with a consecutive partner s[k] (the middle must
        // vanish first) and reduce what follows. Deleting can make
        // the result larger, so I keep the minimum of all options.
        int n = s.Length;
        bool[,] can = new bool[n, n];
        string[,] dp = new string[n, n];
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (len % 2 == 0) {
                    for (int m = i; m < j; m++) {
                        if (can[i, m] && can[m + 1, j]) { can[i, j] = true; break; }
                    }
                    if (!can[i, j]) {
                        for (int k = i + 1; k <= j; k++) {
                            if (Consec(s[i], s[k]) && (k == i + 1 || can[i + 1, k - 1]) && (k == j || can[k + 1, j])) {
                                can[i, j] = true;
                                break;
                            }
                        }
                    }
                }
                string best = s[i] + (i + 1 <= j ? dp[i + 1, j] : "");
                for (int k = i + 1; k <= j; k++) {
                    if (Consec(s[i], s[k]) && (k == i + 1 || can[i + 1, k - 1])) {
                        string rest = k + 1 <= j ? dp[k + 1, j] : "";
                        if (string.CompareOrdinal(rest, best) < 0) best = rest;
                    }
                }
                dp[i, j] = best;
            }
        }
        return n == 0 ? "" : dp[0, n - 1];
    }

    private static bool Consec(char a, char b) {
        int d = Math.Abs(a - b);
        return d == 1 || d == 25;
    }
}
