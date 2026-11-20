# 3668. Restore Finishing Order (Easy)
# https://leetcode.com/problems/restore-finishing-order/
# Submission 2200039137 — Accepted, Python3
from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # My thinking: keep only the friends, lined up
        # in the same order they finished in.
        friends = set(friends)
        return [x for x in order if x in friends]
