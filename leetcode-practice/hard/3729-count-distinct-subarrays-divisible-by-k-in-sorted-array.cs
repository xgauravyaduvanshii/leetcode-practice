// LeetCode 3729. Count Distinct Subarrays Divisible by K in Sorted Array — Hard
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/
// Submission 2203135246 — Accepted, C#
using System;
using System.Collections.Generic;

public class Solution {
    public long NumGoodSubarrays(int[] nums, int k) {
        // My thinking: prefix sums modulo k count every good
        // subarray by position — two equal remainders bound a
        // subarray whose sum is divisible by k. That over-counts
        // only one kind of duplicate: in a sorted array, a value
        // sequence repeats only when it is all one value inside a
        // run of equal values, where a length-h block appears
        // m - h + 1 times positionally but is one distinct
        // sequence. So count all good subarrays, then walk each
        // maximal run and subtract m - h for every length h whose
        // block sum h * v is divisible by k.
        long ans = 0;
        int s = 0;
        var cnt = new Dictionary<int, int>();
        cnt[0] = 1;
        foreach (int x in nums) {
            s = (s + x) % k;
            cnt.TryGetValue(s, out int c);
            ans += c;
            cnt[s] = c + 1;
        }
        int n = nums.Length;
        int i = 0;
        while (i < n) {
            int j = i + 1;
            while (j < n && nums[j] == nums[i]) j++;
            int m = j - i;
            for (int h = 1; h <= m; h++) {
                if ((long)nums[i] * h % k == 0) {
                    ans -= m - h;
                }
            }
            i = j;
        }
        return ans;
    }
}
