# LeetCode 1817. Finding the Users Active Minutes — Medium
# https://leetcode.com/problems/finding-the-users-active-minutes/
# Submission 2199941134 — Accepted, Python3
#
# My thinking: each user's minutes are a set
# — repeat logins in the same minute count
# once. Then I just tally how many users end
# up with one minute, two minutes, and so on.

from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        active = defaultdict(set)
        for user, minute in logs:
            active[user].add(minute)
        result = [0] * k
        for minutes in active.values():
            result[len(minutes) - 1] += 1
        return result
