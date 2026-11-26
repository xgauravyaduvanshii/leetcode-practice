// LeetCode 4051. Count Subarrays with Distant Sums — Hard
// https://leetcode.com/problems/count-subarrays-with-distant-sums/
// Submission 2203573776 — Accepted, Java
import java.util.Arrays;

class Solution {
    public long distantSubarrays(int[] nums, int goal, int k) {
        // My thinking: write the subarray sum as a difference
        // of prefix sums, sum(nums[i..j]) = pref[j+1] - pref[i].
        // A subarray is distant when its sum is at least k away
        // from goal, so for each right end j the earlier prefix
        // pref[i] must satisfy pref[i] <= pref[j+1] - goal - k
        // or pref[i] >= pref[j+1] - goal + k. Counting how many
        // earlier prefixes fall in those two ranges is a job
        // for a Fenwick tree over the coordinate-compressed
        // prefix sums, since the prefixes are not sorted and
        // can be as large as 1e14. Insert pref[0] first, then
        // for each j query both ranges and insert pref[j+1].
        // When k is 0 every subarray is distant, since an
        // absolute difference is always at least 0, so return
        // n*(n+1)/2 directly (the two ranges would otherwise
        // double-count pref[i] == pref[j+1] - goal).
        int n = nums.length;
        if (k == 0) {
            return (long) n * (n + 1) / 2;
        }
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }
        long[] vals = pref.clone();
        Arrays.sort(vals);
        int m = 0;
        for (int i = 0; i < vals.length; i++) {
            if (i == 0 || vals[i] != vals[i - 1]) {
                vals[m++] = vals[i];
            }
        }
        vals = Arrays.copyOf(vals, m);
        Fenwick ft = new Fenwick(m);
        ft.add(indexOf(vals, pref[0]), 1);
        long ans = 0;
        for (int j = 0; j < n; j++) {
            long cur = pref[j + 1];
            long lo = cur - goal - k;
            long hi = cur - goal + k;
            // prefixes <= lo: count of compressed values <= lo
            ans += ft.sum(upperBound(vals, lo));
            // prefixes >= hi: total seen minus those < hi
            ans += (j + 1) - ft.sum(lowerBound(vals, hi));
            ft.add(indexOf(vals, cur), 1);
        }
        return ans;
    }

    // Number of values in vals strictly less than v.
    private static int lowerBound(long[] vals, long v) {
        int pos = Arrays.binarySearch(vals, v);
        return pos >= 0 ? pos : -pos - 1;
    }

    // Number of values in vals less than or equal to v.
    private static int upperBound(long[] vals, long v) {
        int pos = Arrays.binarySearch(vals, v);
        return pos >= 0 ? pos + 1 : -pos - 1;
    }

    // 1-based Fenwick index of an exact prefix value.
    private static int indexOf(long[] vals, long v) {
        return Arrays.binarySearch(vals, v) + 1;
    }

    private static class Fenwick {
        private final long[] bit;

        Fenwick(int n) {
            bit = new long[n + 1];
        }

        void add(int i, long delta) {
            while (i < bit.length) {
                bit[i] += delta;
                i += i & -i;
            }
        }

        long sum(int i) {
            long s = 0;
            while (i > 0) {
                s += bit[i];
                i -= i & -i;
            }
            return s;
        }
    }
}
