// 3312. Sorted GCD Pair Queries (Hard)
// https://leetcode.com/problems/sorted-gcd-pair-queries/
// Submission 2202322580 -- Accepted, C#
public class Solution {
    public int[] GcdValues(int[] nums, int[] queries) {
        // My thinking: for each d I count how many numbers are divisible by d,
        // which gives the number of pairs whose gcd is a multiple of d. Working
        // down from the largest value and subtracting the counts of the larger
        // multiples of d leaves exactly the pairs whose gcd IS d. A prefix sum
        // over d then turns each query into a binary search for the smallest d
        // whose running pair count passes the query index.
        int maxV = 0;
        foreach (int v in nums) maxV = Math.Max(maxV, v);
        int[] freq = new int[maxV + 1];
        foreach (int v in nums) freq[v]++;
        long[] exact = new long[maxV + 1];
        for (int d = maxV; d >= 1; d--) {
            long divisible = 0;
            for (int mult = d; mult <= maxV; mult += d) divisible += freq[mult];
            long pairs = divisible * (divisible - 1) / 2;
            for (int mult = 2 * d; mult <= maxV; mult += d) pairs -= exact[mult];
            exact[d] = pairs;
        }
        long[] prefix = new long[maxV + 1];
        long run = 0;
        for (int d = 1; d <= maxV; d++) { run += exact[d]; prefix[d] = run; }
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int lo = 1, hi = maxV;
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if (prefix[mid] > queries[i]) hi = mid; else lo = mid + 1;
            }
            ans[i] = lo;
        }
        return ans;
    }
}
