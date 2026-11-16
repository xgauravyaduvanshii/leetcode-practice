# LeetCode 953. Verifying an Alien Dictionary — Easy
# https://leetcode.com/problems/verifying-an-alien-dictionary/
# Submission 2197545815 — Accepted, Python3
#
# My thinking: first I learn the alien order of the
# letters. Then I compare each pair of neighbouring
# words — at the first letter where they differ,
# the earlier word's letter must come first in the
# alien order. If one word is a prefix of the
# other, the shorter one has to come first.

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    if rank[first[j]] > rank[second[j]]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False
        return True
