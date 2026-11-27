# LeetCode 2241. Design an ATM Machine — Medium
# https://leetcode.com/problems/design-an-atm-machine/
# Submission 2204513454 — Accepted, Python3
#
# My thinking: deposits just add to the counts of each denomination.
# For a withdrawal I greedily take as many of the largest notes as
# possible, since using a large note can never hurt the ability to make
# the amount with smaller ones in this denomination set. If the greedy
# pass leaves money over, the withdrawal fails and nothing is taken;
# otherwise I subtract what was used and return the counts.
class ATM:
    def __init__(self):
        self.banknotes = [0] * 5
        self.denoms = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: list[int]) -> None:
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> list[int]:
        used = [0] * 5
        for i in range(4, -1, -1):
            take = min(self.banknotes[i], amount // self.denoms[i])
            used[i] = take
            amount -= take * self.denoms[i]
        if amount != 0:
            return [-1]
        for i in range(5):
            self.banknotes[i] -= used[i]
        return used
