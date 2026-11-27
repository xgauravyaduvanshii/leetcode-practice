// LeetCode 2179. Count Good Triplets in an Array — Hard
// https://leetcode.com/problems/count-good-triplets-in-an-array/
// Submission 2201603541 — Accepted, C#
//
// My thinking: a good triplet rises in both
// orders, so I rewrite the first array by
// each value's place in the second — then
// every middle value counts its smaller
// neighbours on the left times its larger
// neighbours on the right, tallied with a
// Fenwick tree.

public class Solution {
    public long GoodTriplets(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) pos[nums2[i]] = i;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = pos[nums1[i]];
        long[] left = new long[n];
        long[] bit = new long[n + 1];
        for (int j = 0; j < n; j++) {
            left[j] = FenwickSum(bit, a[j] - 1);
            FenwickAdd(bit, a[j], 1);
        }
        long[] right = new long[n];
        bit = new long[n + 1];
        for (int j = n - 1; j >= 0; j--) {
            long seen = n - 1 - j;
            right[j] = seen - FenwickSum(bit, a[j]);
            FenwickAdd(bit, a[j], 1);
        }
        long ans = 0;
        for (int j = 0; j < n; j++) ans += left[j] * right[j];
        return ans;
    }

    private void FenwickAdd(long[] bit, int i, long delta) {
        i += 1;
        while (i < bit.Length) {
            bit[i] += delta;
            i += i & -i;
        }
    }

    private long FenwickSum(long[] bit, int i) {
        long s = 0;
        i += 1;
        while (i > 0) {
            s += bit[i];
            i -= i & -i;
        }
        return s;
    }
}
