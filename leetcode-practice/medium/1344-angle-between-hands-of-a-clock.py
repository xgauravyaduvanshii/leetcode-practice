# LeetCode 1344. Angle Between Hands of a Clock — Medium
# https://leetcode.com/problems/angle-between-hands-of-a-clock/
# Submission 2199036471 — Accepted, Python3
#
# My thinking: the minute hand moves six
# degrees a minute, the hour hand half a degree
# a minute on top of its hour. The answer is
# the smaller of their gap and the rest of the
# circle.

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        minute_angle = minutes * 6
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)
