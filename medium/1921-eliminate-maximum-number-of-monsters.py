# LeetCode 1921. Eliminate Maximum Number of Monsters — Medium
# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
# Submission 2201601759 — Accepted, Python3
#
# My thinking: each monster reaches the city
# after ceil(dist / speed) minutes, so I sort
# those arrival times and kill one monster a
# minute — a monster can only be killed while
# its arrival minute is still strictly ahead
# of the minute I would shoot it.

class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        times = sorted((d + s - 1) // s for d, s in zip(dist, speed))
        ans = 0
        for i, t in enumerate(times):
            if t > i:
                ans += 1
            else:
                break
        return ans
