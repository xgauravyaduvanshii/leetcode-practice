# 3996. Even Number of Knight Moves (Easy)
# https://leetcode.com/problems/even-number-of-knight-moves/
# Submission 2200094312 — Accepted, Python3
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        # My thinking: every knight move flips the
        # colour of the square. After an even number
        # of moves the knight is back on its starting
        # colour — so the trip is possible exactly when
        # start and target share a colour.
        return (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2
