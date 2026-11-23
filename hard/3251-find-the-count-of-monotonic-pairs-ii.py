# LeetCode 3251. Find the Count of Monotonic Pairs II — Hard
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/
# Submission 2202140852 — Accepted, Python3
#
# My thinking: same split as part I — arr1
# non-decreasing, arr2 non-increasing, arr1[i]
# + arr2[i] = nums[i]. The DP over arr1[i] needs
# prefix sums at every step; on the larger limits
# here I build them with C-level accumulate and
# slicing instead of a Python loop, so the same
# transition stays fast enough.

from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        from itertools import accumulate
        MOD = 10 ** 9 + 7
        dp = [1] * (nums[0] + 1)
        for i in range(1, len(nums)):
            d = nums[i] - nums[i - 1]
            need = d if d > 0 else 0
            cum = [x % MOD for x in accumulate(dp)]
            total = cum[-1]
            cur_len = nums[i] + 1
            if need >= cur_len:
                dp = [0] * cur_len
            else:
                ndp = [0] * need + cum[:cur_len - need]
                if len(ndp) < cur_len:
                    ndp += [total] * (cur_len - len(ndp))
                dp = ndp
        return sum(dp) % MOD
