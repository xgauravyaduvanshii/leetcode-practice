# 3158. Find the XOR of Numbers Which Appear Twice (Easy)
# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/
# Submission 2199980308 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        # My thinking: count how often each number shows
        # up, then XOR together the ones that appear
        # exactly twice. Numbers appearing once or three
        # times do not count.
        counts = Counter(nums)
        answer = 0
        for num, count in counts.items():
            if count == 2:
                answer ^= num
        return answer
