// LeetCode 2151. Maximum Good People Based on Statements — Hard
// https://leetcode.com/problems/maximum-good-people-based-on-statements/
// Submission 2201590894 — Accepted, Java
//
// My thinking: with fifteen people at most I
// can just try every possible set of good
// people — a set only stands if every good
// person's word about everyone else matches
// the set, and the biggest set that stands is
// the answer.

class Solution {
    public int maximumGood(int[][] statements) {
        int n = statements.length;
        int best = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            boolean ok = true;
            for (int i = 0; i < n && ok; i++) {
                if ((mask >> i & 1) == 0) continue;
                for (int j = 0; j < n; j++) {
                    if (statements[i][j] == 1 && (mask >> j & 1) == 0) {
                        ok = false;
                        break;
                    }
                    if (statements[i][j] == 0 && (mask >> j & 1) == 1) {
                        ok = false;
                        break;
                    }
                }
            }
            if (ok) best = Math.max(best, Integer.bitCount(mask));
        }
        return best;
    }
}
