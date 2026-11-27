# LeetCode 2049. Count Nodes With the Highest Score — Medium
# https://leetcode.com/problems/count-nodes-with-the-highest-score/
# Submission 2204379210 — Accepted, Python3
#
# My thinking: removing a node splits the tree into the subtree of
# each of its children plus the rest of the tree above it, and its
# score is the product of those part sizes. I build the children
# lists from the parents array, get subtree sizes with one bottom-up
# pass over a DFS order, then score every node from its children's
# sizes and the size of the part above it, counting how many reach
# the best score.
class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            stack.extend(children[u])
        sz = [1] * n
        for u in reversed(order):
            for v in children[u]:
                sz[u] += sz[v]
        best = 0
        cnt = 0
        for u in range(n):
            score = 1
            for v in children[u]:
                score *= sz[v]
            if n - sz[u] > 0:
                score *= n - sz[u]
            if score > best:
                best = score
                cnt = 1
            elif score == best:
                cnt += 1
        return cnt
