// LeetCode 3671. Sum of Beautiful Subsequences — Hard
// https://leetcode.com/problems/sum-of-beautiful-subsequences/
// Submission 2203030172 — Accepted, Java
import java.util.*;

class Solution {
    private static final int MOD = 1000000007;

    public int sumOfBeautifulSubsequences(int[] nums) {
        // My thinking: the answer is the sum of the GCDs of all
        // strictly increasing subsequences, and every integer is the
        // sum of Euler's totient over its divisors, so a subsequence
        // with GCD g contributes phi(d) once for every d dividing g.
        // Swapping the sums, I only need, for each d, how many
        // strictly increasing subsequences use only multiples of d.
        // I group each number's scaled values by its divisors first
        // (walking nums once, in order, so each group's list keeps
        // the original order), then count increasing subsequences
        // per group with a Fenwick tree over the compressed values:
        // each value adds 1 plus all counts of smaller values seen
        // so far. Multiply each group's count by phi(d) and add up.
        // A naive scan of all of nums for every d is too slow, so
        // the divisor grouping is what keeps this fast enough.
        if (nums.length == 0) return 0;
        int maxV = 0;
        for (int v : nums) maxV = Math.max(maxV, v);
        int[] phi = new int[maxV + 1];
        for (int i = 0; i <= maxV; i++) phi[i] = i;
        for (int i = 2; i <= maxV; i++) {
            if (phi[i] == i) {
                for (int j = i; j <= maxV; j += i) {
                    phi[j] -= phi[j] / i;
                }
            }
        }
        List<List<Integer>> groups = new ArrayList<>(maxV + 1);
        for (int i = 0; i <= maxV; i++) groups.add(null);
        for (int v : nums) {
            for (int d = 1; d * d <= v; d++) {
                if (v % d == 0) {
                    addToGroup(groups, d, v / d);
                    if (d * d != v) addToGroup(groups, v / d, d);
                }
            }
        }
        long ans = 0;
        for (int d = 1; d <= maxV; d++) {
            List<Integer> vals = groups.get(d);
            if (vals == null) continue;
            ans = (ans + (long) phi[d] * countIncSubseq(vals)) % MOD;
        }
        return (int) ans;
    }

    private void addToGroup(List<List<Integer>> groups, int d, int scaled) {
        List<Integer> g = groups.get(d);
        if (g == null) {
            g = new ArrayList<>();
            groups.set(d, g);
        }
        g.add(scaled);
    }

    private long countIncSubseq(List<Integer> vals) {
        int[] uniq = vals.stream().distinct().sorted().mapToInt(Integer::intValue).toArray();
        int m = uniq.length;
        long[] bit = new long[m + 2];
        long total = 0;
        for (int x : vals) {
            int idx = Arrays.binarySearch(uniq, x) + 1; // 1-based
            long smaller = 0;
            for (int i = idx - 1; i > 0; i -= i & -i) {
                smaller = (smaller + bit[i]) % MOD;
            }
            long cur = (1 + smaller) % MOD;
            for (int i = idx; i < bit.length; i += i & -i) {
                bit[i] = (bit[i] + cur) % MOD;
            }
            total = (total + cur) % MOD;
        }
        return total;
    }
}
