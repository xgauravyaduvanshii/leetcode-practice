# LeetCode 1916. Count Ways to Build Rooms in an Ant Colony — Hard
# https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/
# Submission 2201231223 — Accepted, Python3
#
# My thinking: a room can only be built after its
# parent, so each subtree contributes its own
# number of orders — I merge children with the
# multinomial coefficient, counting the ways to
# interleave their build orders.

MOD = 10 ** 9 + 7

class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        n = len(prevRoom)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[prevRoom[i]].append(i)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        order = [0]
        stack = [0]
        while stack:
            u = stack.pop()
            for v in children[u]:
                order.append(v)
                stack.append(v)
        size = [0] * n
        ways = [0] * n
        for u in reversed(order):
            total = 0
            w = 1
            for v in children[u]:
                total += size[v]
                w = w * ways[v] % MOD
            w = w * fact[total] % MOD
            for v in children[u]:
                w = w * inv_fact[size[v]] % MOD
            size[u] = total + 1
            ways[u] = w
        return ways[0]
