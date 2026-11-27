# LeetCode 944. Delete Columns to Make Sorted — Easy
# https://leetcode.com/problems/delete-columns-to-make-sorted/
# Submission 2197545483 — Accepted, Python3
#
# My thinking: I check each column on its own — if
# any letter in it is smaller than the one above
# it, that column is out of order and has to be
# deleted. I just count how many columns fail.

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        deletions = 0
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    deletions += 1
                    break
        return deletions
