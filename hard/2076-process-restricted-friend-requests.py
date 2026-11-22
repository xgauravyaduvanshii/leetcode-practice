# LeetCode 2076. Process Restricted Friend Requests — Hard
# https://leetcode.com/problems/process-restricted-friend-requests/
# Submission 2200895181 — Accepted, Python3
#
# My thinking: each person belongs to a group, and two
# people can only become friends if merging their groups
# would not put a restricted pair in the same group.

class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        result = []
        for u, v in requests:
            ru, rv = find(u), find(v)
            ok = True
            if ru != rv:
                for a, b in restrictions:
                    if {find(a), find(b)} == {ru, rv}:
                        ok = False
                        break
            if ok:
                parent[ru] = rv
            result.append(ok)
        return result
