# LeetCode 2611. Mice and Cheese — Medium
# https://leetcode.com/problems/mice-and-cheese/
# Submission 2205102613 — Accepted, Python3
#
# My thinking: start by giving every cheese to the second
# mouse, then hand the first mouse the k cheeses where it
# gains the most over the second — the k largest differences
# reward1[i] - reward2[i].
class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        total = sum(reward2)
        gains = sorted((a - b for a, b in zip(reward1, reward2)), reverse=True)
        return total + sum(gains[:k])
