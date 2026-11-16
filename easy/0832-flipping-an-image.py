# LeetCode 832. Flipping an Image — Easy
# https://leetcode.com/problems/flipping-an-image/
# Submission 2197532751 — Accepted, Python3
#
# My thinking: flipping a row left-to-right is just
# reversing it, and inverting it means turning every
# 0 into a 1 and every 1 into a 0. So for each row
# I reverse it and flip each bit — one line does
# both.

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        return [[1 - x for x in reversed(row)] for row in image]
