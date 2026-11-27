# LeetCode 2029. Stone Game IX — Medium
# https://leetcode.com/problems/stone-game-ix/
# Submission 2204367978 — Accepted, Python3
#
# My thinking: only the remainders mod 3 matter, since the running sum
# mod 3 decides who loses. Stones divisible by 3 never change the sum,
# they just flip whose turn it is to face the other stones. If their
# count is even, the player to move on the 1s and 2s is the same as at
# the start, so Alice needs both a 1 and a 2 available to force Bob
# into a losing move. If it is odd, the turn flips, and Alice wins
# only when the counts of 1s and 2s differ by more than 2, so Bob
# cannot mirror her picks.
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c0 = sum(1 for s in stones if s % 3 == 0)
        c1 = sum(1 for s in stones if s % 3 == 1)
        c2 = sum(1 for s in stones if s % 3 == 2)
        if c0 % 2 == 0: return c1 > 0 and c2 > 0
        return abs(c1 - c2) > 2
