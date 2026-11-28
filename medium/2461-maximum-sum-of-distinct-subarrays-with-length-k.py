# LeetCode 2461. Maximum Sum of Distinct Subarrays With Length K — Medium
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# Submission 2204960084 — Accepted, Python3
#
# My thinking: slide a window of length k, keeping the frequencies
# of its elements and the window sum. A window counts only when all
# k values are distinct — exactly when the frequency map holds k
# entries — and the answer is the largest sum among those windows.
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = {}
        window_sum = 0
        res = 0
        for i, x in enumerate(nums):
            freq[x] = freq.get(x, 0) + 1
            window_sum += x
            if i >= k:
                out = nums[i - k]
                freq[out] -= 1
                if freq[out] == 0:
                    del freq[out]
                window_sum -= out
            if i >= k - 1 and len(freq) == k:
                res = max(res, window_sum)
        return res
