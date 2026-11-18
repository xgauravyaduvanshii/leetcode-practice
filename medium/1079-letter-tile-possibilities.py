# LeetCode 1079. Letter Tile Possibilities — Medium
# https://leetcode.com/problems/letter-tile-possibilities/
# Submission 2198996886 — Accepted, Python3
#
# My thinking: I build every sequence one tile
# at a time, counting each tile I use. Trying
# every remaining letter at each step counts
# every sequence of every length exactly once.

from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = Counter(tiles)

        def build():
            total = 0
            for letter in counts:
                if counts[letter] > 0:
                    counts[letter] -= 1
                    total += 1 + build()
                    counts[letter] += 1
            return total

        return build()
