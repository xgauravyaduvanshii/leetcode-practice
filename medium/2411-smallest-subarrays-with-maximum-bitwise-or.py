# LeetCode 2411. Smallest Subarrays With Maximum Bitwise OR — Medium
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
# Submission 2204792455 — Accepted, Python3
#
# My thinking: the max OR for subarrays starting at i is the OR of the
# whole suffix (suf[i]). For each bit set in suf[i], the answer must
# reach the last occurrence of that bit at or after i (nxt[b]). The
# farthest such position over all set bits gives the shortest subarray
# achieving the max OR.
class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] | nums[i]
        nxt = [n] * 31
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            for b in range(31):
                if (nums[i] >> b) & 1:
                    nxt[b] = i
            j = i
            x = suf[i]
            for b in range(31):
                if (x >> b) & 1:
                    j = max(j, nxt[b])
            ans[i] = j - i + 1
        return ans
