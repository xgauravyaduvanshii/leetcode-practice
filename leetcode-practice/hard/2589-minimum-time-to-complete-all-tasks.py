# LeetCode 2589. Minimum Time to Complete All Tasks — Hard
# https://leetcode.com/problems/minimum-time-to-complete-all-tasks/
# Submission 2201846382 — Accepted, Python3
#
# My thinking: I handle the tasks in
# the order their windows close, and
# whenever one is still short of its
# hours I switch the computer on at the
# latest free seconds inside its window
# — those late seconds are the ones the
# next tasks can still share.

class Solution:
    def findMinimumTime(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        on = [False] * 2001
        total = 0
        for start, end, duration in tasks:
            have = sum(on[start:end + 1])
            need = duration - have
            t = end
            while need > 0 and t >= start:
                if not on[t]:
                    on[t] = True
                    total += 1
                    need -= 1
                t -= 1
        return total
