# LeetCode 791. Custom Sort String — Medium
# https://leetcode.com/problems/custom-sort-string/
# Submission 2198938718 — Accepted, Python3
#
# My thinking: each letter's place is given by
# its position in the order string, and letters
# not in it go last. Sorting by that rank puts
# the string in the custom order.

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank = {ch: i for i, ch in enumerate(order)}
        return "".join(sorted(s, key=lambda ch: rank.get(ch, len(order))))
