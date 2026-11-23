# LeetCode 3181. Maximum Total Reward Using Operations II — Hard
# https://leetcode.com/problems/maximum-total-reward-using-operations-ii/
# Submission 2202064807 — Accepted, Python3
#
# My thinking: a total x is reachable
# when some reward v can be taken from a
# total below v. I track reachable totals
# as a bitset: for each distinct v, the
# new totals are the old totals below v
# shifted by v. Python's big integers
# make the shift one operation; the
# answer is the highest set bit.

from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        dp = 1
        for v in sorted(set(rewardValues)):
            if v >= dp.bit_length():
                dp |= dp << v
            else:
                dp |= (dp & ((1 << v) - 1)) << v
        return dp.bit_length() - 1
