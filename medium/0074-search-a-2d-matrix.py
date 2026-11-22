# LeetCode 74. Search a 2D Matrix — Medium
# https://leetcode.com/problems/search-a-2d-matrix/
# Submission 2201079992 — Accepted, Python3
#
# My thinking: the whole grid reads like one sorted list
# if I flatten it in my head, so I binary-search that
# list and translate each index back to a row and a column.

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // cols][mid % cols]
            if value == target:
                return True
            if value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
