# LeetCode 495. Teemo Attacking — Easy
# https://leetcode.com/problems/teemo-attacking/
# Submission 2197484451 — Accepted, Python3
#
# My thinking: each attack poisons for `duration`
# seconds, unless the next attack lands sooner — then
# the poison only lasts until that next attack. So
# for every pair of attacks I add the smaller of the
# gap and the duration, plus one full duration for
# the last attack.

class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries) - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration
