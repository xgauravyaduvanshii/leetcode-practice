// LeetCode 3739. Count Subarrays With Majority Element II — Hard
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/
// Submission 2203141953 — Accepted, Java
class Solution {
    private int[] bit;
    private int size;

    private void add(int i, int delta) {
        for (; i <= size; i += i & -i) {
            bit[i] += delta;
        }
    }

    private int prefix(int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) {
            s += bit[i];
        }
        return s;
    }

    public long countMajoritySubarrays(int[] nums, int target) {
        // My thinking: write target as +1 and every other value
        // as -1, so target is the majority of a subarray exactly
        // when that subarray sums to more than 0. With prefix
        // sums, a subarray ending here is good exactly when an
        // earlier prefix sum is smaller than the current one, so
        // I keep the earlier prefix sums in a Fenwick tree over
        // the shifted range [-n, n] and count how many of them
        // sit below the current sum as I sweep the array once.
        int n = nums.length;
        size = 2 * n + 1;
        bit = new int[size + 2];
        add(n + 1, 1);
        int s = 0;
        long ans = 0;
        for (int x : nums) {
            s += x == target ? 1 : -1;
            ans += prefix(s + n);
            add(s + n + 1, 1);
        }
        return ans;
    }
}
