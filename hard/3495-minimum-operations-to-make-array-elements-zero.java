// LeetCode 3495. Minimum Operations to Make Array Elements Zero — Hard
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/
// Submission 2202715532 — Accepted, Java
class Solution {
    public long minOperations(int[][] queries) {
        // My thinking: an element x needs t(x) touches, where t(x)
        // is how many times it must be divided by 4 to reach 0, so
        // t(x) = k exactly on [4^(k-1), 4^k - 1]. One operation
        // touches two elements, and the largest t(x) is only about
        // 15 while the total is huge, so the touches can always be
        // paired up with no operation wasting both touches on one
        // element. A query therefore costs ceil(total touches / 2),
        // and I get the total from a prefix sum over the powers
        // of 4.
        long[] pow4 = new long[16];
        pow4[0] = 1;
        for (int i = 1; i < 16; i++) pow4[i] = pow4[i - 1] * 4;
        long[] pref = new long[16];
        pref[0] = 0;
        for (int i = 1; i < 16; i++) {
            pref[i] = pref[i - 1] + (long) i * (pow4[i] - pow4[i - 1]);
        }
        long ans = 0;
        for (int[] q : queries) {
            long total = F(q[1], pow4, pref) - F(q[0] - 1, pow4, pref);
            ans += (total + 1) / 2;
        }
        return ans;
    }

    private long F(long X, long[] pow4, long[] pref) {
        if (X <= 0) return 0;
        int k = 1;
        while (k < pow4.length && pow4[k] <= X) k++;
        return pref[k - 1] + (long) k * (X - pow4[k - 1] + 1);
    }
}
