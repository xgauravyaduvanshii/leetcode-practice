# LeetCode 2075. Decode the Slanted Ciphertext — Medium
# https://leetcode.com/problems/decode-the-slanted-ciphertext/
# Submission 2204399122 — Accepted, Python3
#
# My thinking: the text was written row by row into a grid of the
# given rows and then read diagonally, so I read it back along the
# same diagonals: starting from each column of the first row, walk
# down-right collecting characters, then do the same for the diagonals
# that start in the first column below the first row. Trailing spaces
# are padding, so I strip them from the result.
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        res = []
        for j in range(cols):
            i = 0
            while i < rows and j + i < cols:
                res.append(encodedText[i * cols + j + i])
                i += 1
        for i in range(1, rows):
            j = 0
            while i < rows and j < cols:
                res.append(encodedText[i * cols + j])
                i += 1
                j += 1
        return ''.join(res).rstrip()
