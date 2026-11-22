# LeetCode 1862. Sum of Floored Pairs — Hard
# https://leetcode.com/problems/sum-of-floored-pairs/
# Submission 2201205995 — Accepted, Python3
#
# My thinking: for each value used as a divisor
# I walk its multiples and count how many numbers
# fall in each quotient band — every such number
# pairs with every copy of the divisor at that
# quotient.

MOD = 10 ** 9 + 7

class Solution:
    def sumOfFlooredPairs(self, nums: list[int]) -> int:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for v in nums:
            cnt[v] += 1
        pref = [0] * (mx + 2)
        for i in range(1, mx + 1):
            pref[i] = pref[i - 1] + cnt[i]
        ans = 0
        for d in range(1, mx + 1):
            if cnt[d] == 0:
                continue
            for mult in range(d, mx + 1, d):
                hi = min(mult + d - 1, mx)
                c = pref[hi] - pref[mult - 1]
                ans = (ans + (mult // d) * c * cnt[d]) % MOD
        return ans
