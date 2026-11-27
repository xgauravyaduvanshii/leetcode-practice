# LeetCode 2250. Count Number of Rectangles Containing Each Point — Medium
# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/
# Submission 2204517049 — Accepted, Python3
#
# My thinking: a rectangle contains a point when its height is at least
# the point's y and its length is at least the point's x. I group the
# rectangle lengths by height and sort each group, then for a point I
# look at every height from y up to 100 and binary-search how many
# lengths in that group reach x.
class Solution:
    def countRectangles(self, rectangles: list[list[int]], points: list[list[int]]) -> list[int]:
        import bisect
        by_height = [[] for _ in range(101)]
        for l, h in rectangles:
            by_height[h].append(l)
        for h in range(101):
            by_height[h].sort()
        ans = []
        for x, y in points:
            cnt = 0
            for h in range(y, 101):
                lst = by_height[h]
                if lst:
                    cnt += len(lst) - bisect.bisect_left(lst, x)
            ans.append(cnt)
        return ans
