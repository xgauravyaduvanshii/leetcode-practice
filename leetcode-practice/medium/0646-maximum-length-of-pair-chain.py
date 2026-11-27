# LeetCode 646. Maximum Length of Pair Chain — Medium
# https://leetcode.com/problems/maximum-length-of-pair-chain/
# Submission 2198891839 — Accepted, Python3
#
# My thinking: sorting the pairs by their right
# end lets me be greedy — take the pair that ends
# earliest and still starts after the last one I
# took, and it never hurts the chain.

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda pair: pair[1])
        length = 0
        end = float("-inf")
        for left, right in pairs:
            if left > end:
                length += 1
                end = right
        return length
