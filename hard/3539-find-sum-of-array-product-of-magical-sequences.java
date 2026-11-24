// LeetCode 3539. Find Sum of Array Product of Magical Sequences — Hard
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/
// Submission 2202819748 — Accepted, Java
import java.util.*;

class Solution {
    static final int MOD = 1000000007;
    public int magicalSum(int m, int k, int[] nums) {
        // My thinking: a sequence is fixed by how many times each
        // index is used, and the sum 2^seq[0] + ... is read bit by
        // bit with carries: at index j, choosing c copies contributes
        // c + carry to that bit, whose parity is a set bit and whose
        // half carries on. I walk the indices keeping (carry, set
        // bits so far, elements used) and multiply by C(remaining, c)
        // times nums[j]^c, which is exactly the multinomial weight
        // of the sequences with that count. At the end the leftover
        // carry's own set bits are added to the count.
        int n = nums.length;
        long[][] C = new long[m + 1][m + 1];
        for (int i = 0; i <= m; i++) {
            C[i][0] = C[i][i] = 1;
            for (int j = 1; j < i; j++) C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
        long[][] pw = new long[n][m + 1];
        for (int j = 0; j < n; j++) {
            pw[j][0] = 1;
            for (int c = 1; c <= m; c++) pw[j][c] = pw[j][c - 1] * nums[j] % MOD;
        }
        Map<Long, Long> dp = new HashMap<>();
        dp.put(0L, 1L);
        for (int j = 0; j < n; j++) {
            Map<Long, Long> ndp = new HashMap<>();
            for (Map.Entry<Long, Long> e : dp.entrySet()) {
                long key = e.getKey();
                int carry = (int)(key >> 40);
                int bits = (int)((key >> 20) & 0xFFFFF);
                int used = (int)(key & 0xFFFFF);
                long val = e.getValue();
                int rem = m - used;
                for (int c = 0; c <= rem; c++) {
                    int s = c + carry;
                    int ncarry = s / 2;
                    int nbits = bits + (s % 2);
                    if (nbits > k) continue;
                    int nused = used + c;
                    long factor = C[rem][c] * pw[j][c] % MOD;
                    long nkey = ((long)ncarry << 40) | ((long)nbits << 20) | nused;
                    ndp.merge(nkey, val * factor % MOD, (a, b) -> (a + b) % MOD);
                }
            }
            dp = ndp;
        }
        long ans = 0;
        for (Map.Entry<Long, Long> e : dp.entrySet()) {
            long key = e.getKey();
            int carry = (int)(key >> 40);
            int bits = (int)((key >> 20) & 0xFFFFF);
            int used = (int)(key & 0xFFFFF);
            if (used == m && bits + Integer.bitCount(carry) == k) {
                ans = (ans + e.getValue()) % MOD;
            }
        }
        return (int)ans;
    }
}
