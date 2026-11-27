# LeetCode 2003. Smallest Missing Genetic Value in Each Subtree — Hard
# https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/
# Submission 2201307240 — Accepted, Python3
#
# My thinking: only the nodes above the 1 can
# miss anything but 1, so I walk up from the 1
# gathering each new branch once — the missing
# value only ever climbs.

class Solution:
    def smallestMissingValueSubtree(self, parents: list[int], nums: list[int]) -> list[int]:
        n = len(parents)
        children = [[] for _ in range(n)]
        node1 = -1
        for i, p in enumerate(parents):
            if p != -1:
                children[p].append(i)
            if nums[i] == 1:
                node1 = i
        ans = [1] * n
        if node1 == -1:
            return ans
        seen = set()
        mex = 1

        def add_subtree(u):
            stack = [u]
            while stack:
                x = stack.pop()
                seen.add(nums[x])
                for c in children[x]:
                    stack.append(c)

        add_subtree(node1)
        node = node1
        while True:
            while mex in seen:
                mex += 1
            ans[node] = mex
            p = parents[node]
            if p == -1:
                break
            seen.add(nums[p])
            for c in children[p]:
                if c != node:
                    add_subtree(c)
            node = p
        return ans
