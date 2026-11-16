# LeetCode 599. Minimum Index Sum of Two Lists — Easy
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Submission 2197504006 — Accepted, Python3
#
# My thinking: I remember where each word sits in
# the first list. Then I walk the second list — for
# every word that appears in both, I add up its two
# positions. I keep the smallest total I have seen,
# and all the words that tie for it.

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index = {word: i for i, word in enumerate(list1)}
        best = float('inf')
        result = []
        for j, word in enumerate(list2):
            if word in index:
                total = index[word] + j
                if total < best:
                    best = total
                    result = [word]
                elif total == best:
                    result.append(word)
        return result
