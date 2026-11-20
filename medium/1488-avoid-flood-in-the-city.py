# LeetCode 1488. Avoid Flood in The City — Medium
# https://leetcode.com/problems/avoid-flood-in-the-city/
# Submission 2199860719 — Accepted, Python3
#
# My thinking: when a lake fills twice, some
# dry day after its first fill must drain it. I
# keep the dry days sorted and always take the
# earliest one that comes after the last fill.

import bisect
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full = {}
        dry_days = []
        answer = []
        for day, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(day)
                answer.append(1)
            else:
                answer.append(-1)
                if lake in full:
                    index = bisect.bisect_right(dry_days, full[lake])
                    if index == len(dry_days):
                        return []
                    dry_day = dry_days.pop(index)
                    answer[dry_day] = lake
                full[lake] = day
        return answer
