# LeetCode 508. Most Frequent Subtree Sum — Medium
# https://leetcode.com/problems/most-frequent-subtree-sum/
# Submission 2198834127 — Accepted, Python3
#
# My thinking: every subtree has a sum, and I count
# how often each sum appears while computing them
# bottom-up. The sums with the highest count are
# the answer.

from collections import Counter
from typing import List


class Solution:
    def findFrequentTreeSum(self, root) -> List[int]:
        counts = Counter()

        def subtree_sum(node):
            if not node:
                return 0
            total = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            counts[total] += 1
            return total

        subtree_sum(root)
        highest = max(counts.values())
        return [total for total, count in counts.items() if count == highest]
