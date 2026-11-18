# LeetCode 437. Path Sum III — Medium
# https://leetcode.com/problems/path-sum-iii/
# Submission 2198794786 — Accepted, Python3
#
# My thinking: a path from some ancestor to this
# node sums to the target exactly when an earlier
# running total was this total minus the target. I
# count how often each running total has appeared
# on the way down, and remove it again on the way
# back up.

from collections import defaultdict


class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1

        def count_paths(node, running_sum):
            if not node:
                return 0
            running_sum += node.val
            total = prefix_counts[running_sum - targetSum]
            prefix_counts[running_sum] += 1
            total += count_paths(node.left, running_sum)
            total += count_paths(node.right, running_sum)
            prefix_counts[running_sum] -= 1
            return total

        return count_paths(root, 0)
