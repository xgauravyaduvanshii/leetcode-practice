// LeetCode 3630. Partition Array for Maximum XOR and AND — Hard
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/
// Submission 2202891156 — Accepted, Java
class Solution {
    public int maximizeXorAndXor(int[] nums) {
        // My thinking: I fix the AND part B and split the rest S
        // between A and C. With X the xor of all of S, the best
        // split scores X plus twice the most I can pull out of the
        // bits where X is zero, and that best comes from a linear
        // basis of S: scanning bits from high to low, I take a
        // basis vector whenever it turns on a zero-bit of X. I try
        // every choice of B (at most 2^19 of them) and keep the
        // best total.
        int n = nums.length;
        int best = 0;
        for (int maskB = 0; maskB < (1 << n); maskB++) {
            int andB = -1;
            int xorS = 0;
            int[] sElems = new int[n];
            int sLen = 0;
            for (int i = 0; i < n; i++) {
                if ((maskB >> i & 1) == 1) {
                    andB = andB == -1 ? nums[i] : (andB & nums[i]);
                } else {
                    xorS ^= nums[i];
                    sElems[sLen++] = nums[i];
                }
            }
            if (andB == -1) andB = 0;
            int[] basis = new int[30];
            for (int k = 0; k < sLen; k++) {
                int x = sElems[k];
                for (int b = 29; b >= 0; b--) {
                    if ((x >> b & 1) == 0) continue;
                    if (basis[b] == 0) {
                        basis[b] = x;
                        break;
                    }
                    x ^= basis[b];
                }
            }
            int a = 0;
            for (int b = 29; b >= 0; b--) {
                if (((xorS >> b) & 1) == 0 && ((a >> b) & 1) == 0 && basis[b] != 0) {
                    a ^= basis[b];
                }
            }
            int xorSum = xorS + 2 * (a & ~xorS);
            best = Math.max(best, andB + xorSum);
        }
        return best;
    }
}
