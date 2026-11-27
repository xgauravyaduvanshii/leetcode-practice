# LeetCode 1943. Describe the Painting — Medium
# https://leetcode.com/problems/describe-the-painting/
# Submission 2201761690 — Accepted, Python3
#
# My thinking: every segment only changes
# the mix at its two ends — I record the
# colour added at each start and removed
# at each end, then walk the line left to
# right, merging the stretches where the
# running mix stays the same, so two
# neighbouring stretches with the same
# mix become one segment.

class Solution:
    def splitPainting(self, segments: list[list[int]]) -> list[list[int]]:
        events = {}
        for start, end, color in segments:
            events[start] = events.get(start, 0) + color
            events[end] = events.get(end, 0) - color
        ans = []
        cur = 0
        prev = None
        for pos in sorted(events):
            if prev is not None and cur != 0:
                if ans and ans[-1][2] == cur and ans[-1][1] == prev:
                    ans[-1][1] = pos
                else:
                    ans.append([prev, pos, cur])
            cur += events[pos]
            prev = pos
        return ans
