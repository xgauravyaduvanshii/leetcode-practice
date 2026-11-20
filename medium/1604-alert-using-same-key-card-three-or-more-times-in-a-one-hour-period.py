# LeetCode 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period — Medium
# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
# Submission 2199891281 — Accepted, Python3
#
# My thinking: I turn every time into minutes
# and sort each person's stamps. Any three
# stamps inside a 60-minute window trigger
# the alert.

from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hours, minutes = time.split(":")
            times[name].append(int(hours) * 60 + int(minutes))
        alerted = []
        for name in sorted(times):
            stamps = sorted(times[name])
            for i in range(len(stamps) - 2):
                if stamps[i + 2] - stamps[i] <= 60:
                    alerted.append(name)
                    break
        return alerted
