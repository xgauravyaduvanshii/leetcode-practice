# 821. Shortest Distance to a Character (Easy)
# https://leetcode.com/problems/shortest-distance-to-a-character/
# Submission 2199964768 — Accepted, Python3
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # My thinking: first sweep left to right and note
        # how far each spot is from the nearest c on its
        # left; then sweep right to left and take the
        # smaller of that and the distance to the nearest
        # c on the right.
        n = len(s)
        answer = [0] * n
        prev = -10 ** 9
        for i, ch in enumerate(s):
            if ch == c:
                prev = i
            answer[i] = i - prev
        prev = 10 ** 9
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)
        return answer
