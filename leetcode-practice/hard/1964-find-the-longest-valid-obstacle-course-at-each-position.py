# LeetCode 1964. Find the Longest Valid Obstacle Course at Each Position — Hard
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
# Submission 2201274023 — Accepted, Python3
#
# My thinking: I keep the smallest possible tail
# of a non-decreasing run of each length — each
# new height lands just after the equal heights,
# so it extends the longest run it can, and its
# answer is that length.

import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        d = []
        ans = []
        for x in obstacles:
            pos = bisect.bisect_right(d, x)
            if pos == len(d):
                d.append(x)
            else:
                d[pos] = x
            ans.append(pos + 1)
        return ans
