# LeetCode 2509. Cycle Length Queries in a Tree — Hard
# https://leetcode.com/problems/cycle-length-queries-in-a-tree/
# Submission 2201790334 — Accepted, Python3
#
# My thinking: in this tree a node's
# parent is just half its number, so I
# lift the deeper of the two up until
# they meet at the same depth, then lift
# them together until they meet — the
# steps up plus the new edge between
# them is the cycle.

class Solution:
    def cycleLengthQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        def depth(x):
            d = 0
            while x > 1:
                x //= 2
                d += 1
            return d

        ans = []
        for a, b in queries:
            da, db = depth(a), depth(b)
            steps = 0
            while da > db:
                a //= 2
                da -= 1
                steps += 1
            while db > da:
                b //= 2
                db -= 1
                steps += 1
            while a != b:
                a //= 2
                b //= 2
                steps += 2
            ans.append(steps + 1)
        return ans
