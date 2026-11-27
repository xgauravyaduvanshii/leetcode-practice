# LeetCode 2127. Maximum Employees to Be Invited to a Meeting — Hard
# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/
# Submission 2201581614 — Accepted, Python3
#
# My thinking: everyone points at a favourite,
# so the picture is rings with chains hanging
# off them — a ring of three or more stands
# alone, but a mutual pair can take the two
# longest chains feeding into it, and all the
# mutual pairs can come at once.

from collections import deque


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        n = len(favorite)
        indeg = [0] * n
        for f in favorite:
            indeg[f] += 1
        # Peel off the chains; what stays behind is in rings.
        q = deque(i for i in range(n) if indeg[i] == 0)
        chain = [0] * n
        in_ring = [True] * n
        while q:
            u = q.popleft()
            in_ring[u] = False
            v = favorite[u]
            chain[v] = max(chain[v], chain[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
        # Every mutual pair plus its two chains can come together.
        pair_total = 0
        longest_ring = 0
        seen = [False] * n
        for i in range(n):
            if not in_ring[i] or seen[i]:
                continue
            ring = []
            u = i
            while not seen[u]:
                seen[u] = True
                ring.append(u)
                u = favorite[u]
            if len(ring) == 2:
                a, b = ring
                pair_total += 2 + chain[a] + chain[b]
            else:
                longest_ring = max(longest_ring, len(ring))
        return max(pair_total, longest_ring)
