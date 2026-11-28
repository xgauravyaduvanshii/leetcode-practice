# LeetCode 2545. Sort the Students by Their Kth Score — Medium
# https://leetcode.com/problems/sort-the-students-by-their-kth-score/
# Submission 2205057338 — Accepted, Python3
#
# My thinking: sort the rows by the k-th column, highest first.
# Python's sort is stable, so equal scores keep their order.
class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        return sorted(score, key=lambda row: row[k], reverse=True)
