# LeetCode 3027. Find the Number of Ways to Place People II — Hard
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/
# Submission 2201900803 — Accepted, Python3
#
# My thinking: I sort the points by x
# rising, and for equal x by y falling,
# so Alice comes before every possible
# Bob to her right. For one Alice, I
# walk rightwards keeping the highest y
# seen so far below her: a Bob counts
# exactly when his y is a new high,
# because any lower Bob would have that
# higher point sitting inside his fence.

from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0
        for i in range(n):
            xi, yi = points[i]
            highest = -10**18
            for j in range(i + 1, n):
                xj, yj = points[j]
                if yj > yi:
                    continue
                if yj > highest:
                    ans += 1
                    highest = yj
        return ans
