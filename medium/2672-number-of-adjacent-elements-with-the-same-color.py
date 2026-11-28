# LeetCode 2672. Number of Adjacent Elements With the Same Color — Medium
# https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/
# Submission 2205117073 — Accepted, Python3
#
# My thinking: recolouring one cell only affects the pairs
# with its two neighbours. Before changing it, drop the pairs
# it formed with its old colour; after changing it, add the
# pairs it forms with its new colour. The running total is
# the answer after every query.
class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        colors = [0] * n
        ans = []
        same = 0
        for idx, color in queries:
            if colors[idx] == color:
                ans.append(same)
                continue
            for nb in (idx - 1, idx + 1):
                if 0 <= nb < n and colors[nb] != 0:
                    if colors[nb] == colors[idx]:
                        same -= 1
                    if colors[nb] == color:
                        same += 1
            colors[idx] = color
            ans.append(same)
        return ans
