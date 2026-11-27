# LeetCode 2171. Removing Minimum Number of Magic Beans — Medium
# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/
# Submission 2204486589 — Accepted, Python3
#
# My thinking: after removing beans, every non-empty bag must hold the
# same number of beans, and emptying a bag is allowed. If I sort the
# bags and pick one bag's count as the target, every smaller bag is
# emptied and every larger bag is trimmed down to it. I try each bag as
# the target and keep the smallest removal total.
class Solution:
    def minimumRemoval(self, beans: list[int]) -> int:
        beans.sort()
        total = sum(beans)
        n = len(beans)
        best = total
        for i, b in enumerate(beans):
            kept = b * (n - i)
            removed = total - kept
            if removed < best:
                best = removed
        return best
