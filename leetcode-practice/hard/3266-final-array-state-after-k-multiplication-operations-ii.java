// LeetCode 3266. Final Array State After K Multiplication Operations II — Hard
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/
// Submission 2202161012 — Accepted, Java
//
// My thinking: always multiply the smallest
// element, which a heap gives in order. Once
// the smallest times the multiplier passes the
// current maximum, the heap order stops changing
// — the remaining k operations just cycle through
// all n elements evenly. So I simulate only until
// that point, then hand out the leftover
// multiplications round-robin with fast modular
// powers instead of simulating them one by one.

class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        final long MOD = 1000000007L;
        int n = nums.length;
        int[] res = new int[n];
        if (multiplier == 1) {
            for (int i = 0; i < n; i++) res[i] = (int)(nums[i] % MOD);
            return res;
        }
        long[] cur = new long[n];
        long maxV = 0;
        for (int i = 0; i < n; i++) {
            cur[i] = nums[i];
            if (cur[i] > maxV) maxV = cur[i];
        }
        java.util.PriorityQueue<long[]> pq = new java.util.PriorityQueue<>((a, b) -> a[0] != b[0] ? Long.compare(a[0], b[0]) : Long.compare(a[1], b[1]));
        for (int i = 0; i < n; i++) pq.offer(new long[]{cur[i], i});
        while (k > 0) {
            long[] top = pq.peek();
            if (top[0] * multiplier > maxV) break;
            pq.poll();
            long nv = top[0] * multiplier;
            cur[(int)top[1]] = nv;
            pq.offer(new long[]{nv, top[1]});
            k--;
        }
        if (k == 0) {
            for (int i = 0; i < n; i++) res[i] = (int)(cur[i] % MOD);
            return res;
        }
        java.util.List<long[]> order = new java.util.ArrayList<>(pq);
        order.sort((a, b) -> a[0] != b[0] ? Long.compare(a[0], b[0]) : Long.compare(a[1], b[1]));
        long q = k / n;
        int r = k % n;
        for (int rank = 0; rank < order.size(); rank++) {
            int idx = (int)order.get(rank)[1];
            long exp = q + (rank < r ? 1 : 0);
            res[idx] = (int)((cur[idx] % MOD) * modPow(multiplier, exp, MOD) % MOD);
        }
        return res;
    }
    private long modPow(long base, long exp, long mod) {
        long result = 1 % mod;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) result = result * base % mod;
            base = base * base % mod;
            exp >>= 1;
        }
        return result;
    }
}
