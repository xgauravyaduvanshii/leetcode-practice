# LeetCode 2452. Words Within Two Edits of Dictionary — Medium
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/
# Submission 2204950038 — Accepted, Python3
#
# My thinking: a query matches a dictionary word when the two words
# differ in at most two positions, so compare each query against
# every dictionary word and stop at the first match. Short-circuit
# the comparison as soon as a third difference appears.
class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        res = []
        for q in queries:
            for w in dictionary:
                diff = 0
                for a, b in zip(q, w):
                    if a != b:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    res.append(q)
                    break
        return res
