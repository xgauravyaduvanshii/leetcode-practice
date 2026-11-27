# LeetCode 3287. Find the Maximum Sequence Value of Array — Hard
# https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/
# Submission 2202180629 — Accepted, Python3
#
# My thinking: split the array at some point,
# take k elements from the left part and k from
# the right, and maximise OR(left) XOR OR(right).
# For each side I keep, as a 128-bit mask, every
# OR value reachable with exactly k picks —
# OR-ing a new element just shifts the mask's
# bits, which I do with a precomputed table per
# bit. Then every split pairs the reachable ORs
# from its prefix and suffix.

from typing import List


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        all_mask = (1 << 128) - 1
        without = []
        for b in range(7):
            mask = 0
            for v in range(128):
                if not (v >> b) & 1:
                    mask |= 1 << v
            without.append(mask)

        def trans(m: int, x: int) -> int:
            for b in range(7):
                if (x >> b) & 1:
                    w = without[b]
                    m = (m & (~w & all_mask)) | ((m & w) << (1 << b))
            return m

        def bits_of(m: int):
            out = []
            while m:
                lsb = m & -m
                out.append(lsb.bit_length() - 1)
                m ^= lsb
            return out

        pref = [0] * n
        dp = [0] * (k + 1)
        dp[0] = 1
        for i, x in enumerate(nums):
            up = min(i + 1, k)
            for t in range(up, 0, -1):
                if dp[t - 1]:
                    dp[t] |= trans(dp[t - 1], x)
            pref[i] = dp[k]
        suff = [0] * n
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(n - 1, -1, -1):
            x = nums[i]
            up = min(n - i, k)
            for t in range(up, 0, -1):
                if dp[t - 1]:
                    dp[t] |= trans(dp[t - 1], x)
            suff[i] = dp[k]
        ans = 0
        for i in range(n - 1):
            if pref[i] and suff[i + 1]:
                for a in bits_of(pref[i]):
                    for b in bits_of(suff[i + 1]):
                        val = a ^ b
                        if val > ans:
                            ans = val
                            if ans == 127:
                                return 127
        return ans
