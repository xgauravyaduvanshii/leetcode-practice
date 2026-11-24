// LeetCode 3410. Maximize Subarray Sum After Removing All Occurrences of One Element — Hard
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/
// Submission 2202514959 — Accepted 660/660, C#
//
public class Solution {
    public long MaxSubarraySum(int[] nums) {
        // My thinking: deleting all of one value x cuts the array
        // into blocks of non-x elements, and any best subarray of
        // what is left either sits inside one block — then plain
        // Kadane on the original array already covers it — or spans
        // several blocks, in which case it is a suffix of the first
        // block, whole blocks in the middle, and a prefix of the
        // last block. A sparse table over the prefix sums gives each
        // block's best prefix and suffix in O(1), so one sweep per
        // value finds its best spanning subarray; the total work
        // over all values is O(n log n).
        int n = nums.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];

        // Best subarray sum with no deletion (plain Kadane).
        long cur = nums[0], best = nums[0];
        for (int i = 1; i < n; i++) {
            cur = cur < 0 ? nums[i] : cur + nums[i];
            if (cur > best) best = cur;
        }
        long ans = best;

        // Sparse tables for range min / max of the prefix sums.
        int size = n + 1;
        int[] logs = new int[size + 1];
        for (int i = 2; i <= size; i++) logs[i] = logs[i / 2] + 1;
        int levels = logs[size] + 1;
        long[][] stMin = new long[levels][];
        long[][] stMax = new long[levels][];
        stMin[0] = pref;
        stMax[0] = pref;
        for (int j = 1; j < levels; j++) {
            int step = 1 << (j - 1);
            int len = size - (1 << j) + 1;
            stMin[j] = new long[len];
            stMax[j] = new long[len];
            for (int i = 0; i < len; i++) {
                stMin[j][i] = Math.Min(stMin[j - 1][i], stMin[j - 1][i + step]);
                stMax[j][i] = Math.Max(stMax[j - 1][i], stMax[j - 1][i + step]);
            }
        }
        long RangeMin(int lo, int hi) {
            int k = logs[hi - lo + 1];
            return Math.Min(stMin[k][lo], stMin[k][hi - (1 << k) + 1]);
        }
        long RangeMax(int lo, int hi) {
            int k = logs[hi - lo + 1];
            return Math.Max(stMax[k][lo], stMax[k][hi - (1 << k) + 1]);
        }

        var positions = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!positions.TryGetValue(nums[i], out var list)) {
                list = new List<int>();
                positions[nums[i]] = list;
            }
            list.Add(i);
        }

        foreach (var pos in positions.Values) {
            // Blocks are the stretches between consecutive
            // occurrences of this value (and the two ends).
            long total = 0;  // sum of the block sums seen so far
            long bestU = 0;  // best (max suffix - block sums so far)
            bool hasBestU = false;
            int prev = -1;
            for (int t = 0; t <= pos.Count; t++) {
                int p = t < pos.Count ? pos[t] : n;
                int a = prev + 1, b = p - 1;
                if (a <= b) {
                    long blockSum = pref[b + 1] - pref[a];
                    // Best suffix of this block: pref[b + 1] minus
                    // the smallest prefix sum inside the block.
                    long suffix = pref[b + 1] - RangeMin(a, b);
                    // Best prefix of this block: largest prefix sum
                    // just past the block minus pref[a].
                    long prefix = RangeMax(a + 1, b + 1) - pref[a];
                    if (hasBestU) {
                        long cand = total + prefix + bestU;
                        if (cand > ans) ans = cand;
                    }
                    total += blockSum;
                    long val = suffix - total;
                    if (!hasBestU || val > bestU) {
                        bestU = val;
                        hasBestU = true;
                    }
                }
                prev = p;
            }
        }
        return ans;
    }
}
