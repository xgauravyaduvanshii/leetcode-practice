# LeetCode 2522. Partition String Into Substrings With Values at Most K — Medium
# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/
# Submission 2204983557 — Accepted, Python3
#
# My thinking: greedily grow the current substring digit by digit.
# Any digit larger than k makes the whole string impossible; as
# soon as the running value passes k, cut before the last digit and
# start a new substring with it. Greedy is optimal here because a
# longer first piece can only leave less room later.
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        parts = 1
        cur = 0
        for ch in s:
            d = ord(ch) - 48
            if d > k:
                return -1
            cur = cur * 10 + d
            if cur > k:
                parts += 1
                cur = d
        return parts
