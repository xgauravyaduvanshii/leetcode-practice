# LeetCode 1409. Queries on a Permutation With Key — Medium
# https://leetcode.com/problems/queries-on-a-permutation-with-key/
# Submission 2199050849 — Accepted, Python3
#
# My thinking: I keep the permutation as a
# list. Each query looks up the number's spot,
# records it, and moves the number to the front.

from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        order = list(range(1, m + 1))
        result = []
        for query in queries:
            index = order.index(query)
            result.append(index)
            order.pop(index)
            order.insert(0, query)
        return result
