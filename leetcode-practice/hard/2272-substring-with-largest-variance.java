// LeetCode 2272. Substring With Largest Variance — Hard
// https://leetcode.com/problems/substring-with-largest-variance/
// Submission 2201650144 — Accepted, Java
//
// My thinking: for one ordered pair of
// letters the variance is just a signed
// running total, so I sweep every pair and
// keep the best stretch that holds at
// least one of the losing letter.

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int largestVariance(String s) {
        int n = s.length();
        Set<Character> present = new HashSet<>();
        for (int i = 0; i < n; i++) present.add(s.charAt(i));
        int ans = 0;
        for (char a : present) {
            for (char b : present) {
                if (a == b) continue;
                int[] pref = new int[n + 1];
                for (int i = 0; i < n; i++) {
                    int d = s.charAt(i) == a ? 1 : (s.charAt(i) == b ? -1 : 0);
                    pref[i + 1] = pref[i] + d;
                }
                int[] prefMin = new int[n + 1];
                prefMin[0] = pref[0];
                for (int k = 1; k <= n; k++) {
                    prefMin[k] = Math.min(prefMin[k - 1], pref[k]);
                }
                int lastB = -1;
                for (int i = 1; i <= n; i++) {
                    if (s.charAt(i - 1) == b) lastB = i - 1;
                    if (lastB >= 0) {
                        ans = Math.max(ans, pref[i] - prefMin[lastB]);
                    }
                }
            }
        }
        return ans;
    }
}
