# LeetCode 661. Image Smoother — Easy
# https://leetcode.com/problems/image-smoother/
# Submission 2197511259 — Accepted, Python3
#
# My thinking: for each cell I look at its 3x3
# neighbourhood — the cell itself plus its
# neighbours, skipping any that fall outside the
# image — add them all up and divide by how many
# there were (rounding down).

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        total += img[x][y]
                        count += 1
                result[i][j] = total // count
        return result
