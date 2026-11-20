# 3492. Maximum Containers on a Ship (Easy)
# https://leetcode.com/problems/maximum-containers-on-a-ship/
# Submission 2200021698 — Accepted, Python3
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        # My thinking: the deck holds n by n containers
        # at most, and the weight limit allows only so
        # many. The answer is whichever limit is
        # smaller.
        return min(n * n, maxWeight // w)
