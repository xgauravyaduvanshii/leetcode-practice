# LeetCode 2106. Maximum Fruits Harvested After at Most K Steps — Hard
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
# Submission 2201575827 — Accepted, Python3
#
# My thinking: a walk that covers a stretch of
# fruit goes one way first and then back, so
# the cheapest way to cover any stretch is the
# shorter of the two turnarounds — and as the
# right end moves out, the left end only ever
# moves out too, so one sliding window finds
# the richest stretch.

class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix = [0] * (n + 1)
        for i, (_, amount) in enumerate(fruits):
            prefix[i + 1] = prefix[i] + amount

        def steps(l, r):
            lp = fruits[l][0]
            rp = fruits[r][0]
            if rp <= startPos:
                return startPos - lp
            if lp >= startPos:
                return rp - startPos
            go_left_first = 2 * (startPos - lp) + (rp - startPos)
            go_right_first = 2 * (rp - startPos) + (startPos - lp)
            return min(go_left_first, go_right_first)

        ans = 0
        left = 0
        for right in range(n):
            while left <= right and steps(left, right) > k:
                left += 1
            ans = max(ans, prefix[right + 1] - prefix[left])
        return ans
