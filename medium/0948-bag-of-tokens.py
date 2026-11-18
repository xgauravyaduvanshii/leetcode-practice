# LeetCode 948. Bag of Tokens — Medium
# https://leetcode.com/problems/bag-of-tokens/
# Submission 2198973904 — Accepted, Python3
#
# My thinking: I play the cheapest token face up
# whenever I can afford it, and only sell the
# most expensive token when I am stuck and have
# score to spare. The best score I ever hold is
# the answer.

from collections import deque
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        queue = deque(tokens)
        score = best = 0
        while queue:
            if power >= queue[0]:
                power -= queue.popleft()
                score += 1
                best = max(best, score)
            elif score > 0:
                power += queue.pop()
                score -= 1
            else:
                break
        return best
