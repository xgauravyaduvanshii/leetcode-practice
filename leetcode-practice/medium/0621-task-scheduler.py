# LeetCode 621. Task Scheduler — Medium
# https://leetcode.com/problems/task-scheduler/
# Submission 2198880173 — Accepted, Python3
#
# My thinking: the most frequent task sets the
# shape of the schedule — its runs are separated
# by cooling gaps. The answer is either that
# shaped schedule or just the number of tasks,
# whichever is bigger.

from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        busiest = sum(1 for count in counts.values() if count == max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + busiest)
