# LeetCode 733. Flood Fill — Easy
# https://leetcode.com/problems/flood-fill/
# Submission 2197523309 — Accepted, Python3
#
# My thinking: I remember the colour I started on,
# then spread from the starting cell to its four
# neighbours, painting each one and spreading
# further — but only into cells that still have
# the original colour. If the starting colour is
# already the new colour, there is nothing to do.

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        m, n = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != original:
                return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
