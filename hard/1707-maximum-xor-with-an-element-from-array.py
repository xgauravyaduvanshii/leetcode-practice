# LeetCode 1707. Maximum XOR With an Element From Array — Hard
# https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
# Submission 2201103250 — Accepted, Python3
#
# My thinking: I sort the numbers and the queries by
# their limits, then grow a binary trie with every
# number the current limit allows — each query is then
# answered by walking the trie down the opposite bit
# at every step to maximise the xor.

class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        trie = {}
        def insert(num):
            node = trie
            for bit in range(30, -1, -1):
                b = (num >> bit) & 1
                node = node.setdefault(b, {})
        def best_xor(num):
            node = trie
            result = 0
            for bit in range(30, -1, -1):
                b = (num >> bit) & 1
                if 1 - b in node:
                    result |= 1 << bit
                    node = node[1 - b]
                else:
                    node = node[b]
            return result
        nums.sort()
        order = sorted(range(len(queries)), key=lambda i: queries[i][1])
        answer = [0] * len(queries)
        n = 0
        for i in order:
            xi, mi = queries[i]
            while n < len(nums) and nums[n] <= mi:
                insert(nums[n])
                n += 1
            answer[i] = best_xor(xi) if trie else -1
        return answer
