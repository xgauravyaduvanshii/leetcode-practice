# 3360. Stone Removal Game (Easy)
# https://leetcode.com/problems/stone-removal-game/
# Submission 2200007834 — Accepted, Python3
class Solution:
    def canAliceWin(self, n: int) -> bool:
        # My thinking: Alice takes 10 stones, Bob takes
        # 9, then 8, then 7, and so on — each turn takes
        # one fewer stone. Whoever cannot take their
        # share loses, so I just play it out.
        take = 10
        alice_turn = True
        while n >= take:
            n -= take
            take -= 1
            alice_turn = not alice_turn
        return not alice_turn
