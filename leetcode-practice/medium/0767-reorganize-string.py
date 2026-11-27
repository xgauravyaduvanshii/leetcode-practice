# LeetCode 767. Reorganize String — Medium
# https://leetcode.com/problems/reorganize-string/
# Submission 2198931489 — Accepted, Python3
#
# My thinking: the most frequent letter must be
# spread out first — if it appears more than half
# the time, no answer exists. I always place the
# letter with the most remaining copies that is
# not the one I just used.

from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""
        heap = [(-count, ch) for ch, count in counts.items()]
        heapq.heapify(heap)
        result = []
        previous = (0, "")
        while heap:
            count, ch = heapq.heappop(heap)
            result.append(ch)
            if previous[0] < 0:
                heapq.heappush(heap, previous)
            previous = (count + 1, ch)
        return "".join(result)
