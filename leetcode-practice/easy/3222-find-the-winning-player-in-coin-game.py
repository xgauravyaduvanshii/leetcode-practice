# 3222. Find the Winning Player in Coin Game (Easy)
# https://leetcode.com/problems/find-the-winning-player-in-coin-game/
# Submission 2199988432 — Accepted, Python3
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        # My thinking: each turn spends one 75-coin and
        # four 10-coins, so the game lasts as many turns
        # as the smaller of those two piles allows. Alice
        # starts, so an odd number of turns means she
        # takes the last one and Bob loses — otherwise
        # Alice runs out first.
        turns = min(x, y // 4)
        return "Alice" if turns % 2 == 1 else "Bob"
