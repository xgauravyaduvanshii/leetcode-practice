# LeetCode 2405. Optimal Partition of String — Medium
# https://leetcode.com/problems/optimal-partition-of-string/
# Submission 2204785931 — Accepted, Python3
#
# My thinking: greedily cut a new partition whenever the next character
# already appeared in the current one — a partition must have unique
# characters, and cutting as late as possible never hurts because the
# repeated character has to start a new partition anyway.
class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 1
        for ch in s:
            if ch in seen:
                count += 1
                seen = {ch}
            else:
                seen.add(ch)
        return count
