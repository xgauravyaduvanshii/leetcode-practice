# LeetCode 1938. Maximum Genetic Difference Query — Hard
# https://leetcode.com/problems/maximum-genetic-difference-query/
# Submission 2201250619 — Accepted, Python3
#
# My thinking: I walk the family tree keeping a
# binary trie of the ancestors' values — at each
# node I read off the best xor from the trie, then
# add the node, visit its children, and take it
# back out again.

class Solution:
    def maxGeneticDifference(self, parents: list[int], queries: list[list[int]]) -> list[int]:
        n = len(parents)
        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)
        trie = [[-1, -1, 0]]

        def add(num, delta):
            node = 0
            trie[node][2] += delta
            for b in range(29, -1, -1):
                bit = (num >> b) & 1
                if trie[node][bit] == -1:
                    trie[node][bit] = len(trie)
                    trie.append([-1, -1, 0])
                node = trie[node][bit]
                trie[node][2] += delta

        def query_max_xor(num):
            node = 0
            res = 0
            for b in range(29, -1, -1):
                bit = (num >> b) & 1
                want = 1 - bit
                if trie[node][want] != -1 and trie[trie[node][want]][2] > 0:
                    res |= (1 << b)
                    node = trie[node][want]
                else:
                    node = trie[node][bit]
            return res

        by_node = [[] for _ in range(n)]
        for qi, (node, val) in enumerate(queries):
            by_node[node].append((qi, val))
        ans = [0] * len(queries)
        stack = [(root, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                add(node, 1)
                for qi, val in by_node[node]:
                    ans[qi] = query_max_xor(val)
                stack.append((node, 1))
                for child in reversed(children[node]):
                    stack.append((child, 0))
            else:
                add(node, -1)
        return ans
