# LeetCode 1286. Iterator for Combination — Medium
# https://leetcode.com/problems/iterator-for-combination/
# Submission 2199023465 — Accepted, Python3
#
# My thinking: the combinations of the letters
# come in dictionary order, so I build them all
# up front and hand them out one at a time.

from itertools import combinations


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combos = ["".join(c) for c in combinations(characters, combinationLength)]
        self.index = 0

    def next(self) -> str:
        result = self.combos[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combos)
