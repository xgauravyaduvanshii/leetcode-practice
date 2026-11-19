# LeetCode 1405. Longest Happy String — Medium
# https://leetcode.com/problems/longest-happy-string/
# Submission 2199050485 — Accepted, Python3
#
# My thinking: I always take the letter with
# the most left, unless it would make three in
# a row — then I take the next most common one
# instead. A max-heap keeps the richest letter
# on top.

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, ch in ((a, "a"), (b, "b"), (c, "c")):
            if count:
                heapq.heappush(heap, (-count, ch))
        result = []
        while heap:
            count, ch = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == ch:
                if not heap:
                    break
                count2, ch2 = heapq.heappop(heap)
                result.append(ch2)
                if count2 + 1 < 0:
                    heapq.heappush(heap, (count2 + 1, ch2))
                heapq.heappush(heap, (count, ch))
            else:
                result.append(ch)
                if count + 1 < 0:
                    heapq.heappush(heap, (count + 1, ch))
        return "".join(result)
